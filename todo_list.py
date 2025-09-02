from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
hoje = datetime.today()
dia_semana = hoje.strftime("%a").upper()

print('='* 5, ' TODO LIST ', '='*5)
print(hoje.date().today(), "\t", dia_semana)