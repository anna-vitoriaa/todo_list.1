import locale
import tarefas

t = tarefas.Tarefas()
locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
dia_semana = t.d.strftime("%a").upper()

print('='* 5, ' TODO LIST ', '='*5)
print(t.hoje, "\t", dia_semana)
