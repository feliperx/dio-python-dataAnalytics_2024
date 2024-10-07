value = int(input('Informe o número: '))

if value > 50:
    print(f'{value} é maior que 50!')
elif value < 50:
    print(f'{value} é menor que 50!')
else: print('entrou no else!')

#if tenario
positive_number = True if value > 0 else False
print(positive_number)
