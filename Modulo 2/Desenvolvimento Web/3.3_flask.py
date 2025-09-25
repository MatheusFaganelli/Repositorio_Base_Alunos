from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def index():
    return 'hello flask'


@app.route('/sobre')
def sobre():
    return 'hello flask'


@app.route('/idade/<int:idade>')
def idade(idade): 
    return render_template('ex_3-3.html', idade=idade)


if __name__=='__main__':
    app.run(debug=True)