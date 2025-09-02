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
    
    def mostrar_tarefas_dia(self):
        for i, v in enumerate(self.tarefas):

            if v['data'] == self.hoje:
                
                if v['sit'] == False:
                    print('[ ]', end=' ')
                else: 
                    print('[x]', end=' ')

                print(v['nome'])
            

    def remover_tarefa(self, id):
        t = self.tarefas[id]
        self.tarefas.remove(t)
        return 'Tarefa removida'
    
    def editar_tarefa(self, id, nome, data, sit):
        old = self.tarefas[id]
        self.tarefas[id] = {'nome': nome, 'data': data, 'sit': sit}
        return 'Antiga:', old, '\n', 'Atualizada: ', self.tarefas[id]


        