from flask import (Flask, request) #Importa o flask

app = Flask(__name__) #Cria uma instância

@app.route("/", methods=('GET' ,)) #Assina uma rota
def index (): #Função responsavel pela página
    nome = request.args.get('nome')
    #HTML retornado
    return f"""<h1>Pagina Inicial</h1> 
    <p>Olá {nome}, que nome bonito!<p>
    """
@app.route("/outra_pagina", methods=( 'GET', )) 
def outra():
   return "<h1>Outra página</h1>"

@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>GALERIA</h1>" 

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>CONTATO</h1>" 

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre...</h1>" 



@app.route("/area/<float:altura>/<float:largura>", methods=('GET',))
def area(altura: float, largura: float):
    return f"""<h1>A área informada> L={largura}*A={altura} => Área={largura*altura}</h1>"""


@app.route("/numero/<float:parimpar>", methods=('GET',))
def numero(parimpar: float):
  if numero % 2 == 0:
    return f"O número é par."
  else:
    return f"O número é ímpar."

@app.route("/sobrenome/<string:nome>/<string:sobrenome>", methods=('GET',))
def nomesobrenome(nome: str, sobrenome: str):
  return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""


@app.route("/potencia/<float:numero>/<float:elevado>", methods=('GET',))
def potencia(numero: float, elevado: float):
    return f"""<h1>A potencia é> N={numero}** E={elevado} => Potencia={numero**elevado}</h1>"""

@app.route("/tabuada/<int:num>", methods=['GET'])
def tabuada(num: int):   
    html="<ul>"  
    for i in range (1,11):
      html+=f"<li> {num}x{i}={num*i}</li>"
    return html + '</ul>'

@app.route("/tabuada")
@app.route("/tabuada/<numero>",methods=("GET",))
def tabuada(numero = None): # None desobriga o valor
    
    if 'numero' in request.args: # se argumento existir
        numero = request.args.get('numero') # atualiza numero

    return render_template('tabuada.html', numero=numero)