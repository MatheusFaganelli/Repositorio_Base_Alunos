#exercicio 2.1: HTML basico na resposta

# modifique sua rota peincipal pra retornar um pequeno HTML com tiulo paragrafo e um link para outra rota
#.

from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('ex_2-1.html')


@app.route('/sobre')
def sobre():
    return 'ola meu nome é matheus faganelli'


@app.route('/zezinho')
def zezinho():
    return 'acho a rota'

if __name__=='__main__':
    app.run(debug=True)