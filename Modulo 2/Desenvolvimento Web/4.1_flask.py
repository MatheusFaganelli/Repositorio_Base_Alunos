from flask import Flask, render_template

app=Flask(__name__)
@app.route('/', method=['post','get'])
def index():
    if request.method == "post":
        nome= request.form['nome']
        return f'ola {nome}! seja, bem vindo a fabrica'
    return render_template('ex_4-1.html')




if __name__=='__main__':
    app.run(debug=True)