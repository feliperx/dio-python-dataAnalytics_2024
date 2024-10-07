text = input('Informe uma palavra: ')
VOWELS = "AEIOU"

for character in text:
    if character.upper() in VOWELS:
        print(character, end=" ")
print()

#range
for number in range(0, 11):
    print(number, end=" ")

print()

for odd_number in range(1, 25, 2):
    print(odd_number, end=" ")

print("\n")

#while
opcao = 1
while opcao != 0:
    opcao = int(input('>>>> Informe a opcao <<<<\n[1] Continuar\n[0] Sair\n'))
