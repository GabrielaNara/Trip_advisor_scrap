# Trip_advisor_scrap
Scraping Data from Trip Advisor comments about attractions in Brazil

Esse método utiliza o webdriver Selenium e BeautifulSoup em python para raspagem de dados de comentários do TripAdvisor. Para utilizar em outros idiomas atenção para os separadoresde texto e o final ".com.br/"

Todas as informações raspadas são públicas, em atenção à política de privacidade do site TripAvisor. Não são coletados quaisquer tipos de dados pessoais ou sensíveis em atenção à LGPD (Lei Geral de Proteção de Dados).

O método contém trechos com alta probabilidade de falhas a cada atualização no website de origem. Os trechos mais sensíveis do código:

	# Postagem completa de cada pessoa
	attrs={"data-automation":"reviewCard"})

	# URL da postagem
	"a" > "href", attrs={"target":"_blank"}

	#O texto da postagem foi separado por frases que sempre aparecem. Por exemplo o número de contribuições do usuário e o "Leia mais" no final das postagens. 
