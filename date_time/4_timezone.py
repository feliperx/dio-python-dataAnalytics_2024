import pytz
from datetime import datetime, timezone, timedelta

# usando pytz
data_hora1 = datetime.now(pytz.timezone("Europe/Oslo"))
data_hora2 = datetime.now(pytz.timezone("America/Manaus"))
print(data_hora1)
print(data_hora2)

# usando datetime
data_hora3 = datetime.now(timezone(timedelta(hours=2))) # Oslo
data_hora4 = datetime.now(timezone(timedelta(hours=-3))) # Manaus
print(data_hora3)
print(data_hora4)