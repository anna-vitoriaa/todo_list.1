class Tarefas:
    def __init__(self):
        from datetime import datetime
        from os import system
        self.s = system
        self.d = datetime.today()
        self.hoje = datetime.strftime(self.d, "%d/%m/%Y")
        self.situacao = False
        self.tarefas = []
        self.datetime = datetime
    
    def criar_tarefa(self, nome, data):
        tarefa = {'nome': nome, 'data': data, 'sit': self.situacao}
        self.tarefas.append(tarefa)
        return 'Tarefa criada'
    
    def mostrar_tarefas(self):
        print('='*23)
        for i, v in enumerate(self.tarefas):
            sts = '[x]' if v['sit'] else '[ ]'
            print(i, sts, v['nome'])
        print('='*23)

    def remover_tarefa(self, id):
        t = self.tarefas[id]
        self.tarefas.remove(t)
        return 'Tarefa removida'
    
    def editar_tarefa(self, id, nome, data):
        self.tarefas[id] = {'nome': nome, 'data': self.datetime.strftime(data, '%d/%m/%Y'), 'sit': self.situacao}
        return "Tarefa editada"

    def des_marcar(self, id):
        if self.tarefas[id]['sit'] == False:
            self.tarefas[id]['sit'] = True
        else:
            self.tarefas[id]['sit'] = False