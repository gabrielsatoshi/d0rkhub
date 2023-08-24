import requests
from bs4 import BeautifulSoup

# URL target
url = "http://www.teakstore.com.br/produtos.php?cat=%27"

# Faça uma requisição HTTP para obter os dados da página
response = requests.get(url)

# Extraia o conteúdo da página
html_text = response.text
soup = BeautifulSoup(html_text, "html.parser")

# Encontre a <body> e extraia o conteúdo da página
content = soup.body.text

print(content)
