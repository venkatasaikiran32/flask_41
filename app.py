from flask import Flask,render_template,request

app=Flask(__name__)


@app.route('/')
def home():
    return "welcome to pw skills"

@app.route('/<variable>') 
def var_param(variable):
    return render_template('show.html',value=variable)


if __name__=='__main__':
    app.run(debug=True)
