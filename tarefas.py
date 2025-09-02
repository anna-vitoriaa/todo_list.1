class Tarefas:
    def __init__(self):
        from datetime import datetime
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
        for i, v in enumerate(self.tarefas):
            print(i, end=' ')
            if v['sit'] == False:
                print('[ ]', end=' ')
            else: 
                print('[x]', end=' ')

            print(v['nome'])

    def remover_tarefa(self, id):
        t = self.tarefas[id]
        self.tarefas.remove(t)
        return 'Tarefa removida'
    
    def editar_tarefa(self, id, nome, data):
        old = self.tarefas[id]
        self.tarefas[id] = {'nome': nome, 'data': self.datetime.strftime(data, '%d/%m/%Y'), 'sit': self.situacao}
        return 'Antiga:', old, '\n', 'Atualizada: ', self.tarefas[id]

    def des_marcar(self, id):
        if self.tarefas[id]['sit'] == False:
            self.tarefas[id]['sit'] = True
        else:
            self.tarefas[id]['sit'] = False