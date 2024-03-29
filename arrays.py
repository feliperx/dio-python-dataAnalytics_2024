list1 = ['Vasco', 'da', 'Gama']
list2 = list('Vasco')
list3 = list(range(10))
empty_list = []

print(list1)
print(list2)
print(list3)
print(list3[-1])
print(list3[:2])
print(list3[5:])
print(list3[::-1])
print(empty_list)

if empty_list:
    print('entrou')
elif len(empty_list) == 0:
    print(len(empty_list))
    print('entrou elif')
else: print('n entrou')

list4 = list3[::-1]
for index, number in enumerate(list4):
    print(f'{index}: {number}')


#filter
pares = [number for number in list4 if (number % 2 == 0 and number != 0)]
print('pares >>>>', pares)

#map
poww = [number ** 2 for number in list4 if (number % 2 == 0 and number != 0)]
print('pow >>>>', poww)
