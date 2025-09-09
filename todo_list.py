import locale
import UI

ui = UI.Ui()
t = ui.t
locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
dia_semana = t.d.strftime("%a").upper()

print('='* 5, ' TODO LIST ', '='*5)
print(t.hoje, "\t", dia_semana)

t.criar_tarefa(nome="ler", data=t.hoje)
t.criar_tarefa(nome="estudar", data=t.hoje)
t.criar_tarefa(nome="treinar", data=t.hoje)

while True:
    t.mostrar_tarefas()

    op = int(input("\n1\tMarcar\n2\tMenu\n0\tSair\n"))
    if op == 1: ui.print_marcar()
    elif op== 2: ui.print_menu()
    elif op == 0: break
    else: print('Opção Inválida')



