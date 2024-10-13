from datetime import timedelta, datetime, timezone

data_hora = datetime.now()
data_hora_utc = datetime.now(timezone.utc)
data = datetime.now().date()

data_hora_final = data_hora + timedelta(minutes=50) # + minutos
data_hora_final2 = data_hora + timedelta(hours=20) # + 20 horas

print(data_hora)
print(data_hora_utc)
print(data_hora_final)
print(data_hora_final2)
print(data)
