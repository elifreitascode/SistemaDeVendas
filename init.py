from flask import Flask, app
from flask import render_template
app = Flask(__name__)

#criar a primeira página do site 
#route
@app.route('/')
#template
#o que eu quero exibir na página
def login():
    return render_template('login.html')
@app.route('/paginainicial')
def paginaInicial():
    return render_template('paginainicial.html')
#colocar a página no ar
if __name__=='__main_':
    app.run(debug=True)
app.run(debug=True)