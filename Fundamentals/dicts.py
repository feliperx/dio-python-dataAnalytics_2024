car1 = {'model': 'celta', 'color': 'red', 'motor': 1.0}
car2 = dict(model = 'gol', color = 'white', motor = 1.0)
car1['year'] = '2002'
car_store = {
  "peugeot" : {"model": "sw206", "year" : "2023", "color": "silver"},
  "fiat" : {"model": "siena", "year" : "2023", "color": "silver"}
}


print(car1)
print(car2)

car1['color'] = 'black'
print(car1['color'])

print(car_store["fiat"]["model"])
print(car_store["peugeot"]["year"])
print("get >>>> ", car_store.get("peugeot"))
print("get >>>> ", car_store.get("model"))


for key in car2:
  print(car2[key])

#best interation
for key, value in car_store.items():
  print(key, value)

car3 = car1.copy()
print('car3 >>>', car3)
car3.clear()
print('car3 >>>', car3)
