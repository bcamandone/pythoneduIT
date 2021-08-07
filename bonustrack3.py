
personas = {}

while True:
	print("Menú:")
	A= print("Opcion A: Agregar")
	B= print("Opcion B: Mostrar el más chico")
	C= print("Opcion C: Mostrar el más grande")
	D= print("Opcion D: Salir")
	opcion=input("Ingresa una opcion: ")
	if opcion == "A":
		nombre=input("Ingrese un nombre: ")
		edad=int(input("Ingrese la edad: "))
		if nombre == "":
			print("Error ingrese datos correctamente")
		else:
		 personas[nombre] = edad   
		 print("Se han agregado los datos")
	elif opcion== "B":
		aux_edad = 200         
		aux_nombre = ""
		for n in personas:
			if personas[n] < aux_edad:
				aux_edad = personas[n]
				aux_nombre = n
			print(aux_nombre +" es la persona más chica")
	elif opcion== "C":
		aux_edad = 0               
		aux_nombre = ""
		for n in personas:
			if personas[n] > aux_edad:
				aux_edad = personas[n]
				aux_nombre = n
		print(aux_nombre + "es la persona más grande")
	elif opcion == "D":
		print("gracias por utilizar el programa")
		break                  
	else:
		print("Error de opcion")
