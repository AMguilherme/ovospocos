
from server import app
from models import resposta
from flask import jsonify

@app.errorhandler(404)
def tratarNotfound():
    resposta.resposta["Status"]  = "Erro"
    resposta.resposta["Mensagem"] = "Acao nao existente"
    return jsonify(resposta.resposta)


@app.errorhandler(500)
def tratarerrorservidor(error):
    resposta.resposta["Status"] = "Um problema critico foi encontrado. ERRO {0}".format(error)
    return jsonify(resposta.resposta)