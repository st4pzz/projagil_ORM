from flask_restful import Resource
from flask import request, jsonify
from model.biblioteca_modelos import AlunoModel, LivroModel


class ListaAlunos(Resource):

    def get(self):
        todos_alunos = AlunoModel.seach_all()

        lista = []
        for aluno in todos_alunos:
            lista.append(aluno.toDict())

        return {'alunos': lista }


class Aluno(Resource):

    def get(self, id):
        aluno = AlunoModel.find_by_id(id)

        if aluno:
            return aluno.toDict()

        return {'id': None}, 404


    def post(self, id):
        corpo = request.get_json( force=True )

        aluno = AlunoModel(id=id, **corpo) #AlunoModel(corpo['nome'], corpo['numero'])
        try:
            aluno.save()
        except:
            return {"mensagem":"Ocorreu um erro interno ao tentar inserir um aluno (DB)"}, 500

        return aluno.toDict(), 201

    def put(self, id):
        pass
    
    def delete(self, id):
        aluno = AlunoModel.find_by_id(id)

        if aluno:
            aluno.delete()
            return {'mensagem': 'Aluno deletado da base.'}

        return {'mensagem': 'Aluno não encontrado.'}, 404
