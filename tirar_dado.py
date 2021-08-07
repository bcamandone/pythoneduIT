import random 


while true:
	print("Menu")
	print(" 1 - Tirar dado")
	print(" 2 - Salir")
	opcion=(input("Ingrese una opcion: ")
	if opcion == "1":
		numero = random.randint(1,6)
		print("El valor del dado es", numero)

    elif opcion == "2":
		print("Gracias por utilizar el programa")
        break
    else:
		print("Opcion incorrecta, vuelva al Menu")
