import requests

api_key= "2a1ac38a32354cb7b19133643251408"
cidade = input("digite o nome da cidade:").strip()
url= f"api.weatherapi.com/v1/current.json"


#parametrosde requisiçao
parametros ={
    'key':api_key,
    'q':cidade,
    'lang':'pt'#define a resposta como portugues
}
#3 fazer a requisição
resposta = requests.get(url, params=parametros)

# 4. verificar se a requisição foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados['current']['temp_c']
    descrever = dados['current']['condition']['text']
    print(f'temperatura na cidade {cidade}é {temperatura}')
    print(f'descricao: {descrever}')
else:
    print(f'erro na requisição: {resposta.status_code}')
    print( resposta.content)