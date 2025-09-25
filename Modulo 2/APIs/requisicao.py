#comando para instalação do request

import requests
requisicao= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(requisicao)
print(requisicao.status_code)
print(requisicao.json())
print(requisicao.text)
print(requisicao.headers)
print(requisicao.url)
