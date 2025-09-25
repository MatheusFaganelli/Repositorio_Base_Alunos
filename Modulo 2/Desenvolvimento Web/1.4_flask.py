from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return 'ola mundo!'


@app.route('/sobre')
def sobre():
    return 'ola meu nome é matheus e eu sou desenvolvedor python' 

@app.route('/saudacao/<nome>')
def saudaçao(nome):
    return f'ola {nome}! tudo bem'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'o dobro do numero é {numero} é {2*numero}'

if __name__=='__main__':
    app.run(debug=True)
