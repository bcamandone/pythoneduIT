import tkinter as tk

def convertir(dato):
    if dato.isdecimal():
        dato = int(dato)
    else:
        dato = "error"
    return dato

def boton_presionado(): # Obtenemos el texto ingresado por el usuario en cada caja
    # y lo convertimos a un entero para poder sumarlo.
	a= caja1.get()
	b= caja2.get()
	a= convertir(a)
	b = convertir(b)
	if a != "error" and b!="error":
		print(a + b)
	else:
		print("No se puede realizar")
ventana=tk.Tk()
ventana.title("Calculadora")
ventana.config(width=300,height=200)
boton=tk.Button(text="Sumar",command=boton_presionado)
boton.place(x= 40, y=140, width=50, height=40)
caja1 =  tk.Entry()
caja1.place(x= 20, y=40, width=50, height=25)
caja2 =  tk.Entry()
caja2.place(x= 20, y=90, width=50, height=25)
etiqueta1 = tk.Label(text="Ingresa los números a sumar:")
etiqueta1.place(x=25, y=10) 

ventana.mainloop()
