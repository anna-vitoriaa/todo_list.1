class Ui:
    def __init__(self):
        import tarefas
        self.t = tarefas.Tarefas()
    
    def print_marcar(self):
        p = int(input('Qual tarefa quer marcar? '))
        if p >= 0 and p < len(self.t.tarefas):
            self.t.des_marcar(p)
        else: print("Tarefa não encontrada")
        return

    def print_criar(self):
        nome = input("Qual o nome da tarefa? ")
        data = input("Qual a data? (dd/mm/yyyy ou hoje): ")

        if data.upper() == 'HOJE':
            data = self.t.hoje
        elif data[2] == '/' and data[5] == '/':
            data = self.t.datetime.strptime(data, "%d/%m/%Y")
        else: 
            print("Data inválida")
            return
        print(self.t.criar_tarefa(nome= nome, data= data))
        return
    
    def print_editar(self):
        p = int(input('Qual tarefa quer editar? '))
        if p >= 0 and p < len(self.t.tarefas):
            nome = self.t.tarefas[p]['nome']
            data_str = self.t.tarefas[p]['data']
            data = self.t.datetime.strptime(data_str, '%d/%m/%Y')

            print('\nNome: ', nome, '\nData: ', data_str)
            o = int(input("\n1\tNome\n2\tData\nO que você quer mudar? "))
            if 0 < o < 3:
                if o == 1: nome = input("Novo nome: ")
                else: 
                    data = input("Nova data: ")
                    data = self.t.datetime.strptime(data, '%d/%m/%Y')
            else: print("Opção inválida")

            print(self.t.editar_tarefa(id= p, nome= nome, data= data))

        else: print("Tarefa não encontrada")
        return self.print_menu()
    
    def print_deletar(self):
        o = int(input('Qual tarefa quer remover? '))
        if o < len(self.t.tarefas):
            self.t.remover_tarefa(id= o)
        else: 
            print("Tarefa inválida")
            return


    def print_menu(self):
        while True:
            print('\n1\tMarcar tarefa')
            print('2\tCriar tarefa')
            print('3\tEditar tarefa')
            print('4\tDeletar tarefa')
            print('5\tMostrar tarefas')
            print('0\tSair')
            op = int(input('Opção: '))

            match op:
                case 1: self.print_marcar()
                case 2: self.print_criar()
                case 3: self.print_editar()
                case 4: self.print_deletar()
                case 5: self.t.mostrar_tarefas()
                case 0: break
        return

    
