from datetime import datetime
from os import system as s
from datetime import datetime 
import utils as ut

class Tarefas:
    def __init__(self):
        self.d = datetime.today()
        self.hoje_str = datetime.strftime(self.d, "%d/%m/%Y")
        self.situacao = False
        self.tarefas = []
    
    def criar_tarefa(self, nome, data):
        try:
            data = ut.validar_data(data_str= data)
            if data is not None:
                tarefa = {'nome': nome, 'data': data, 'sit': self.situacao}
                self.tarefas.append(tarefa)
                return 'Tarefa criada'
            else: return ("Data inválida")
        except(ValueError):
            print("Inválido")
    
    def mostrar_tarefas(self):
        print('='*23)
        for i, v in enumerate(self.tarefas):
            sts = '[x]' if v['sit'] else '[ ]'
            print(i+1, sts, v['nome'])
        print('='*23)

    def remover_tarefa(self, id):
        try:
            t = self.tarefas[id]
            self.tarefas.remove(t)
            return 'Tarefa removida'
        except(ValueError):
            print("Inválido")
    
    def editar_tarefa(self, id, nome, data):
        try:
            self.tarefas[id] = {'nome': nome, 'data': data, 'sit': self.situacao}
            return "Tarefa editada"
        except(ValueError):
            print("Inválido")

    def des_marcar(self, id):
        try:
            if self.tarefas[id]['sit'] == False:
                self.tarefas[id]['sit'] = True
            else:
                self.tarefas[id]['sit'] = False
        except(ValueError):
            print("Inválido")