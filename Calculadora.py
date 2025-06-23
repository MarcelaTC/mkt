# Calculadora de ROI, ROAS, CPA - versión de consola

import tkinter as tk

print("=== Calculadora para Marketing ===")

# Primera parte: obtención de valores: inversión e ingresos.

def valores():
	try:
		inversion = float(entry_inversion.get())
		ingresos = float(entry_ingresos.get())
		conversiones = float(entry_conversiones.get())
		return inversion, ingresos, conversiones
	except ValueError:
		resultado.set("Por favor ingrese números válidos.")
		return None, None, None


# Segunda parte: Calculadora ROI.

def calcular_todo():
	inversion, ingresos, conversiones = valores()
	if inversion is None or ingresos is None or conversiones is None:
		return 
	try:
		ROI = ((ingresos - inversion) / inversion) * 100
		ROI = round(ROI, 2)
		ROAS = ingresos / inversion
		ROAS = round(ROAS, 2)
		CPA = inversion / conversiones
		CPA = round(CPA, 2)
		mensaje = ""
		if ROI > 0:
			mensaje += (f"ROI: {ROI}% - ¡Buen trabajo! 💰\n")
		elif ROI < 0:
			mensaje += (f"ROI: {ROI}% - Retorno negativo. 📉\n")
		else:
			mensaje += ("ROI: 0% - No has perdido dinero.\n")

		if ROAS >= 1.5:
			mensaje += f"ROAS = {ROAS} - ¡Buen trabajo!\n"
		elif ROAS < 1:
			mensaje += f"ROAS = {ROAS} - Se debe mejorar\n"
		else:
			mensaje += f"ROAS = {ROAS} - Aceptable\n"

		mensaje += f"CPA: ${CPA} por conversión"
		
		resultado.set(mensaje)

	except ZeroDivisionError:
		resultado.set("La inversión no puede ser 0.")



# Quinta parte Interfaz
root = tk.Tk()
root.title("Calculadora de ROI")
root.geometry("500x400")
root.configure(bg="#232323")

#campos de entrada
tk.Label(root, text="Inversión ($):", bg="#232323", fg="white", font=("Arial", 14)).pack(pady=5)
entry_inversion = tk.Entry(root)
entry_inversion.pack(pady=5)

tk.Label(root, text="Ingresos ($):", bg="#232323", fg="white", font=("Arial", 14)).pack(pady=5)
entry_ingresos = tk.Entry(root)
entry_ingresos.pack(pady=5)

tk.Label(root, text="Conversiones ($):", bg="#232323", fg="white", font=("Arial", 14)).pack(pady=5)
entry_conversiones = tk.Entry(root)
entry_conversiones.pack(pady=5)

#Boton personalizado
btn_calcular = tk.Label(
	root,
	text="Calcular ROI, ROAS y CPA",
	bg="#349B64",
	fg="white",
	font=("Arial", 12, "bold"),
	padx=20,
	pady=10,
	cursor="hand2"
)
btn_calcular.bind("<Button-1>", lambda e: calcular_todo())
btn_calcular.pack(pady=15)

# Resultado
resultado = tk.StringVar()
resultado.set("Ingresa los valores y presiona el botón.")
tk.Label(root, textvariable=resultado, bg="#232323", fg="white", font=("Arial", 12), wraplength=380, justify="center").pack(pady=15)

root.mainloop()