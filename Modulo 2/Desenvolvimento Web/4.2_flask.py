from flask import Flask, render_template,request

app=Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        soma = num1 + num2
        return f'A soma de{num1} e {num2} é {soma}.'
    return render_template('ex_4-2.html')




if __name__=='__main__':
    app.run(debug=True)