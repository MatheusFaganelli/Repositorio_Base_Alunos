from flask import Flask

app=Flask(__name__)#representa o nome do arquivo
# o codigo deve ser escrito entre o app e o app.run.
@app.route('/')#decorador de função
def home():
    return 'Ola mundo'


@app.route('/sobre')
def sobre():
    return 'ola meu nome é matheus faganelli'

if __name__=='__main__':
    app.run(debug=True)
