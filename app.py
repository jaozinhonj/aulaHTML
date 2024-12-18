from flask import (Flask, flash, redirect, render_template, request, url_for)

app.secret_key = 'segredo'  # Para utilizar flash messages
app = Flask(_name_) #Cria uma instância

@app.route("/", methods=('GET' ,)) #Assina uma rota
def index (): #Função responsavel pela página
    nome = request.args.get('nome')
    #HTML retornado
    return f"""<h1>Pagina Inicial</h1> <p>Eu sou Mary</p>
    <p>Olá {nome}, que nome bonito!<p>
    """

@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>GALERIA</h1>" 

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>CONTATO</h1>" 

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre...</h1>" 


# Dia 11/10
# Multiplicação
@app.route("/area/<float:altura>/<float:largura>", methods=('GET',))
def area(altura: float, largura: float):
    return f"""<h1>A área informada> L={largura}*A={altura} => Área={largura*altura}</h1>"""

# Número Par ou Impar
@app.route("/numero/<float:parimpar>", methods=('GET',))
def numero(parimpar: float):
  if numero % 2 == 0:
    return f"O número é par."
  else:
    return f"O número é ímpar."

# Nome e Sobrenome 
@app.route("/nome", methods=('GET',))
def nome():
  nome = request.args.get('nome')
  sobrenome = request.args.get('sobrenome')
  return f"""<h1> Resultado </h1>
  <p>{sobrenome},{nome}</p>"""

# 17/10
# Potencia
@app.route("/potencia/<float:numero>/<float:elevado>", methods=('GET',))
def potencia(numero: float, elevado: float):
    return f"""<h1>A potencia é> N={numero}* E={elevado} => Potencia={numero*elevado}</h1>"""

# 18/10
# Tabuada
@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET", ))
def tabuada(numero = None):

  if 'numero' in request.args:
    numero = int(request.args.get('numero'))
  
  return render_template('tabuada.html',numero=numero)