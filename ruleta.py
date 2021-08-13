import time
import random

def par_impar(dato):
    if dato % 2 == 0:
        print("-> Par")
    else:
        print("-> Impar")

def docenas(valor):
	if  1<=valor<=12:
		print("El numero esta en la primer docena")
	elif 13<=valor<=24:
		print("El numero esta en la segunda docena")  
	elif 25<=valor<=36:
		print("El numero esta en la tercer docena")
	else:
		print("Salio el cero")       
        
while True:
	print("Menú")
	print(" 1- Probar Suerte")
	print(" 2- Salir")
	opcion=input("Ingresa una opcion: ")
	if opcion == "1":
		print("Ruleta girando....")
		time.sleep(5)
		print("No va mas")
		time.sleep(2)
		ruleta= random.randint(0,36)
		print("Salió el: ",ruleta)
		par_impar(ruleta)
		docenas(ruleta)
	if opcion=="2":
		print("Gracias por utilizar la ruleta")
		break
else:
		print("Opcion incorrecta, vuelva al Menú")


