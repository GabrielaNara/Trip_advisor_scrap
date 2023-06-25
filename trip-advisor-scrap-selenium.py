#	pip install selenium 
#	pip install BeautifulSoup

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # For ChromeDriver
import pandas as pd

#variáveis para cada parque:
xlsx = pd.ExcelFile("lista_parques.xlsx") 
lista_parques = pd.read_excel(xlsx)

#for i in lista_parques:
    local = lista_parques.iloc[i,0]
    avaliacoes = lista_parques.iloc[i,1]
    a = lista_parques.iloc[i,2]
    print(local)

    #------------------------------------------------------------
    #--------ESSE ARQUIVO GERA UM CSV NA PASTA DO ARQUIVO--------
    #------------------------------------------------------------
    #URL´s information
    #------------------------------------------------------------
    #set informtions about the url
    n = int(avaliacoes/10)*10 + 10
    #Gtting urls of the coments
    urls = []
    urls.append('https://www.tripadvisor.com.br/'+ a)
    for pagina in range(10,n,10):
        a_plus = 'https://www.tripadvisor.com.br/'+ a
        a_plus = a_plus[:(a_plus.find('Reviews')+7)] + '-or%s' %pagina + a_plus[(a_plus.find('Reviews')+7):]
        urls.append(a_plus)
    
    #Initinting the driver
    #------------------------------------------------------------
    # Set the path to the downloaded web driver executable
    webdriver_path = "/chromedriver"
    # Set up the Service object
    service = Service(webdriver_path)
    # Adjust the webdriver size  
    options = Options()
    options.add_argument("window-size=400,800")
    # Create an instance of the webdriver using the Service object
    navegador = webdriver.Chrome(service=service,options=options)  # For ChromeDriver
    print("Initiating Driver")
    
    #Iteract all coments thought URLs
    #------------------------------------------------------------
    dados_parques = []
    for url in urls:
        navegador.get(url)
        '''
        # clicar no botão de aceitar cookies
        time.sleep(4)  # Add a delay before scraping the page to allow for page rendering
        button_aceito = navegador.find_element(By.ID, "onetrust-accept-btn-handler")
        button_aceito.click()
        '''
        # copiar o conteúdo html da página
        time.sleep(1)
        page_content = navegador.page_source
        soup = BeautifulSoup(page_content, 'html.parser')
        
        #tirando as informações das imagens com a tag reviewCard
        parques = soup.find_all("div", attrs={"data-automation":"reviewCard"})
        
        #criando a lista para o pdf
        for parque in parques:
            parque_url = parque.find("a" > "href", attrs={"target":"_blank"}) #talvezmude
            #print(parque_url["href"])
        
            #abstraindo o texto de cada post
            texto = parque.text
            x = texto.count("contribuiç")
            if x == 1:
                texto = str(texto).split("contribuiç")[1].split("Esta avaliação")[0]
                texto_main =  str(texto).split("Leia maisFeita em")[0]
                texto_data = str(texto).split("Leia maisFeita em")[1]
                #print(texto_main)
                print(texto_data)
                dados_parques.append([texto_data,texto_main,parque_url["href"]])
            else: 
                texto_false = str(texto).split("contribuiç")[0] + "contribuiç"
                texto = str(texto).split(texto_false)[1].split("Esta avaliação")[0]
                texto_main =  str(texto).split("Leia maisFeita em")[0]
                texto_data = str(texto).split("Leia maisFeita em")[1]
                #print(texto_main)
                print(texto_data)
                dados_parques.append([texto_data,texto_main,parque_url["href"]])
        print("ok_________%s" %url)
    
    print("Finish!!")
    df = pd.DataFrame(dados_parques, columns = ["data","texto","url"])
    df.to_csv("tripadvisor_%s.csv" %local)
    
    navegador.quit()








