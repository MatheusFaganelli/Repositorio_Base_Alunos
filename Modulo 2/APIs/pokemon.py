#o que faz retorna informações de pokemon como nome tipo habilidades status
request.get('https://pokeapi.co/api/v2/pokemon/blastoise')
print(type(res.text))
print((res.text))
dados_pokemon = res.json()
print(type(dados_pokemon))