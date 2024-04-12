def show_message(name = "Anonimo" ):
   print(f"Ola {name}")

def show_message2(*, name):
   print(f"Ola {name}")

show_message()
show_message("Felipe")

# show_message2("Ronaldo")
show_message(name = "Ronaldo")

