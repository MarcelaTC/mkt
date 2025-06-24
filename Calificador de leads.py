# Calificador de leads

import tkinter as tk

# Interfaz
root = tk.Tk()
root.title("Clasificador de leads")
root.geometry("400x600")
root.configure(bg="#232323")


#Opciones para datos de origen del lead
opcion = tk.StringVar()
opcion.set("")
tk.Label(root, text="Origen del lead:", bg="#232323", fg="white", font=("Arial", 14), justify="left").pack(pady=20)
tk.Radiobutton(root, text="Google Ads", variable=opcion, value= "Google Ads").pack(anchor="w")
tk.Radiobutton(root, text="Instagram", variable=opcion, value= "Instagram").pack(anchor="w")
tk.Radiobutton(root, text="Tiktok", variable=opcion, value= "Tiktok").pack(anchor="w")
tk.Radiobutton(root, text="Youtube", variable=opcion, value= "Youtube").pack(anchor="w")
tk.Radiobutton(root, text="Facebook", variable=opcion, value= "Facebook").pack(anchor="w")

mensaje = tk.StringVar()
def mostrar_opcion():
	seleccion = opcion.get()
	if seleccion:
		mensaje.set(f"Elegiste como origen {seleccion}")
tk.Label(root, textvariable=mensaje, bg="#232323", fg="white", font=("Arial", 12)).pack(pady=5)

def ingresos():
	try:
		ingreso = float(entry_ingresos.get())
		return ingreso
	except ValueError:
		resultado.set("Por favor, ingrese un monto válido.")
		return None
	
#campo de entrada de ingresos
tk.Label(root, text="Ingresos ($):", bg="#232323", fg="white", font=("Arial", 14), justify="left").pack(pady=5)
entry_ingresos = tk.Entry(root)
entry_ingresos.pack(pady=5)


opcion2 = tk.StringVar()
opcion2.set("")
tk.Label(root, text="Nivel de interés:", bg="#232323", fg="white", font=("Arial", 14), justify="left").pack(pady=20)
tk.Radiobutton(root, text="Alto", variable=opcion2, value= "Alto").pack(anchor="w")
tk.Radiobutton(root, text="Medio", variable=opcion2, value= "Medio").pack(anchor="w")
tk.Radiobutton(root, text="Bajo", variable=opcion2, value= "Bajo").pack(anchor="w")


# Resultado
resultado = tk.StringVar()
resultado.set("Ingresa los valores y presiona el botón.")
tk.Label(root, textvariable=resultado, bg="#232323", fg="white", font=("Arial", 12), wraplength=380, justify="center").pack(pady=15)

#Ventana de resultados
def abrir_ventana():

	# Validar el origen:
	origen = opcion.get()
	interes = opcion2.get()
	if not origen:
		resultado.set("Por favor selecciona un origen.")
		return
	
	# Validar el presupuesto
	try:
		ingreso = float(entry_ingresos.get())
	except ValueError:
		resultado.set("Por favor ingresa un monto válido.")
		return

    # Validar el nivel de interés
	if not interes:
		resultado.set("Por favor selecciona un nivel de interés.")
		return
	
	# Clasificar Leads. Valor de ingresos escogido solo por un supuesto.
	if interes == "Alto" and ingreso >= 1000:
		clasificacion = "Lead caliente"
	elif interes == "Medio" and ingreso >= 500:
		clasificacion = "Lead medio"
	else:
		clasificacion = "Lead bajo"
	
	#mostrar mensajes 
	mensaje = (
		f"Origen: {origen}\n"
		f"Ingresos: ${ingreso}\n"
		f"Nivel de interés: {interes}\n\n"
		f"Resultado: {clasificacion}"
	)
	ventana = tk.Toplevel(root)
	ventana.title("Ventana de resultados")
	ventana.geometry("250x150")

	etiqueta = tk.Label(ventana, text=mensaje, bg="#232323", fg="white", font=("Arial", 12), wraplength=280, justify="left")
	etiqueta.pack(pady=20)
	
	boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
	boton_cerrar.pack()

btn = tk.Button(root,text="Confirmar", command=abrir_ventana, font=("Arial", 14))
btn.pack(pady=10)


root.mainloop()