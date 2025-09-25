import requests

cep =input("digite o CEP (somente numeros): ")
url = f"https://viacep.com.br/ws/{cep}/json/"


resposta = requests.get(url)

if resposta.status_code ==200:
      dados = resposta.json()
      if 'erro' not in dados:
        print(f'CEP: {dados['cep']}')
        print(f'longradouro:{dados['logradouro']}')
        print(f'bairro:{dados['bairro']}')
        print(f'cidade:{dados['localidade']}')
        print(f'estado:{dados['uf']}')
      else:
          print('CEP não encontrado.')
else:
    print(f'erro na requisição:{resposta.status_code}')
    print(resposta.content)
    



