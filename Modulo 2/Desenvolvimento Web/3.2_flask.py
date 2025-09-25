


from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def index():
    return 'hello flask'


@app.route('/sobre')
def sobre():
    return 'hello flask'


@app.route('/lista')
def lista():
    alunos=['wellington', 'matheus', 'jose',]
    return render_template('ex_3-2.html', lista=alunos)


if __name__=='__main__':
    app.run(debug=True)










