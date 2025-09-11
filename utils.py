from datetime import datetime

def validar_data(data_str):
    if data_str.upper() == 'HOJE':
        return datetime.today()
    
    try:
        return datetime.strptime(data_str, '%d/%m/%Y')
    except(ValueError):
        return None
    
def validar_id(id, lista):
    id = id-1
    if 0 <= id < len(lista):
        return id
    else: return None