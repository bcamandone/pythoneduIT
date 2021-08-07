def verificar(dato):
    while dato == "":
        print("Error")
        dato = input("Ingrese el dato nuevamente: ")
    return dato

def convertir(valor):
    while valor.isdecimal() == False:
        print("Error")
        valor = input("Ingrese valor nuevamente: ")
    return valor
    
alumnos = {}

while True:
	print("Menu")
	print("1 - Añadir un alumno a la lista")
	print("2 - Ver la lista de alumnos")
	print("3 -  Ver la cantidad de cursos de un alumno")
	print("4 - Salir")
	opcion= int(input("Ingrese un numero de opcion"))
	
	if opcion==1:
		nombre=input("Ingrese el nombre del alumno: ")
		nombre=verificar(nombre)
		cursos= int(input("Ingrese la cantidad de cursos: "))
		cursos= convertir(cursos)
		alumnos[nombre]=cursos
		print("El alumno fue añadido a la lista")
			
	elif opcion==2:
		print("Los alumnos son: ")
		for m in alumno:
			alumnos[nombre] = cursos  
			print(nombre + " - " + str(cursos) + " cursos")
		
	elif opcion == 3:
		name=input("Ingrese el nombre del alumno que desea ver la cantidad de cursos: ")
		if name in almnos:
			print(nombre + "tiene" + str(alumnos([nombre])) + " cursos")
		else:
			print("Alumno sin cursos asignados")
	elif opcion == 4:
		print("¡Gracias por utilizar el programa!") #debo colocar el print antes del break 
		break #fuerzo el bucle a que termine
		
	else: 
		print("La opción ingresada no es correcta")
		


