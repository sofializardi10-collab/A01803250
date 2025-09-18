# éste es un codigo que revisa si la edad es válida

valida = False
while not valida:
  edad = int(input("Cuantos años tienes? "))
  if edad < 100 and edad > 1 :
    print("Perfecto!")
    valida = True 
