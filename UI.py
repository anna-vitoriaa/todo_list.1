import tarefas
import utils 
from datetime import datetime as dt

class Ui:
    t = tarefas.Tarefas()

    def print_marcar(self):
        try: 
            p = int(input('Qual tarefa quer marcar? '))
            id = utils.validar_id(p, self.t.tarefas)
            if id is not None:
                self.t.des_marcar(id)
                return
            print('Id inválido')
        except(ValueError):
            print("Tarefa não encontrada")

    def print_criar(self):
        nome = input("Qual o nome da tarefa? ")
        data_str = input("Qual a data? (dd/mm/yyyy ou hoje): ")
        print(self.t.criar_tarefa(nome= nome, data= data_str))
        return
    
    def print_editar(self):
        p = int(input('Qual tarefa quer editar? '))
        try:
            id = utils.validar_id(p, self.t.tarefas)
            if id is not None:
                print(self.t.tarefas[id]['data'])
                nome = self.t.tarefas[id]['nome']
                data = self.t.tarefas[id]['data']

                print('\nNome: ', nome, '\nData: ', data.strftime('%d/%m/%Y'))
                o = int(input("\n1\tNome\n2\tData\nO que você quer mudar? "))
                if 0 < o < 3:
                    if o == 1: nome = input("Novo nome: ")
                    else: 
                        data_str = input("Nova data: ")
                        data = dt.strptime(data_str, '%d/%m/%Y')
            else: print("Opção inválida")

            print(self.t.editar_tarefa(id= id, nome= nome, data= data))
            return
        except(ValueError):
            print("Tarefa não encontrada")
    
    def print_deletar(self):
        o = int(input('Qual tarefa quer remover? '))
        try:
            id = utils.validar_id(o, self.t.tarefas)
            if id is not None:
                self.t.remover_tarefa(id= id)
            return
        except(ValueError):
            print("Tarefa não encontrada")


    def print_menu(self):
        while True:
            print('\n1\tMarcar tarefa')
            print('2\tCriar tarefa')
            print('3\tEditar tarefa')
            print('4\tDeletar tarefa')
            print('5\tMostrar tarefas')
            print('6\tFiltrar tarefas por dia')
            print('0\tSair')
            op = int(input('Opção: '))

            match op:
                case 1: self.print_marcar()
                case 2: self.print_criar()
                case 3: self.print_editar()
                case 4: self.print_deletar()
                case 5: self.t.mostrar_tarefas()
                case 6: self.print_por_dia()
                case 0: break
                case _: print('Opção inválida')
        return

    def print_por_dia(self):
        while True:
            data = input("Qual dia quer filtrar? (dd/mm/yyyy) ")
            dataf = utils.validar_data(data_str= data)
            if dataf is not None: break
        try:
            print('\n')
            print("="*23)
            print('🗓️  Tarefas de ', dataf.strftime('%d/%m/%Y') if dataf.date() != dt.today().date() else 'Hoje')
            print("="*23)
    
            tarefas_dia = [t for t in self.t.tarefas if t['data'].date() == dataf.date()]
        

            for i, t in enumerate(tarefas_dia):
                sts = '[x]' if t['sit'] else '[ ]'
                print(i+1, sts, t['nome'])
            
            if not tarefas_dia: 
                print("Nenhuma tarefa para este dia")
                return
            
            total = len(tarefas_dia)
            concluidas = sum(t['sit'] for t in self.t.tarefas)
            print("\nTotal de tarefas para hoje: ", total)
            print("Total de tarefas concluídas: ", concluidas)
            print("Total de tarefas pendentes: ", total-concluidas)
            print('='*23)
            return
                    
        except(ValueError):
            print("Formato inválido")
            return


    
