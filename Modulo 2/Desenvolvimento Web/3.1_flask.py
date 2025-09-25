from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('ex_2-2.html')


@app.route('/sobre')
def sobre():
    return 'hello flask'


@app.route('/saudacao/<nome>')
def saudacao(nome):
    return render_template('ex_3-1.html', nome=nom)


@app.route('/dobro/<int:numero>')
def dobro (numero):
    dobro + numero*2
    return f'o dobro de {numero} é {dobro}'


if __name__=='__main__':
    app.run(debug=True)