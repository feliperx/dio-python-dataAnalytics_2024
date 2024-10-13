# Formatadores

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2021-03-21 12:30"
mascara_ptbr = "%d/%m/%Y %a %H:%M:%S"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual)
print(data_hora_atual.strftime(mascara_ptbr))

# transforma para tipo datetime
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(type(data_convertida)) # <class 'datetime.datetime'>

