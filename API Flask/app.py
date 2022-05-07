from flask import Flask, jsonify, request
import json

app = Flask(__name__)

alunos = [
    {
        'id': '0',
        'nome': 'Iago',
        'disciplinas': ['Python', 'Java']
    },
    {
        'id': '1',
        'nome': 'Sarah',
        'disciplinas': ['Python']
    }
]

@app.route('/aluno/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def aluno(id):
    if request.method == 'GET':
        try:
            response = alunos[id]
        except IndexError:
            mensagem = 'Aluno de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        alunos[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        alunos.pop(id)
        return jsonify({'status': 'sucesso!', 'mensagem': 'Registro excluído'})

@app.route('/aluno/', methods=['POST', 'GET'])
def lista_alunos():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(alunos)
        dados['id'] = posicao
        alunos.append(dados)
        return jsonify(alunos[posicao])
    elif request.method == 'GET':
        return jsonify(alunos)

if __name__ == '__main__':
    app.run(debug=True)