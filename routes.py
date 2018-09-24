import server
from flask import jsonify
from services import listar
from models import resposta
from server import app



@app.route("/alunos", methods=["GET"])
def listarroute():
    resposta.resposta["Status"] = "Sucesso"
    resposta.resposta["Dados"] = listar.listar()    
    resposta.resposta["Mensagem"] = "Alunos enviados."
    return jsonify(resposta.resposta)