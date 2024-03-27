text = input('Informe uma palavra: ')
VOWELS = "AEIOU"

for character in text:
    if character.upper() in VOWELS:
        print(character, end=" ")
