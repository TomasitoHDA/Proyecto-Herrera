import tkinter as tk

def calcular_porcentaje( ):
    try:
        cantidad = float(cantidad_entry.get())
        porcentaje = float(porcentaje_entry.get())
        resultado = cantidad * porcentaje / 100
        resultado_label.config(text="El resultado es: {:.2f}".format(resultado))
    except ValueError:
        resultado_label.config(text="Error: ingrese valores numéricos válidos.")

def limpiar_campos():
    cantidad_entry.delete(0, tk.END)
    porcentaje_entry.delete(0, tk.END)
    resultado_label.config(text="El resultado es: ")
    cantidad_entry.focus()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Porcentajera")
ventana.resizable(False, False)
ventana.geometry("250x160")
ventana.config(bg = "#D3D3D3")
ventana.iconbitmap("D:\\Tomas\\Curso pyton\\Proyecto Herrera\\porcentaje.ico")

# Crear los widgets
cantidad_label = tk.Label(ventana, text="Cantidad:")
cantidad_label.config(bg = "#D3D3D3")
cantidad_label.grid(row=0, column=0, padx=5, pady=5)

cantidad_entry = tk.Entry(ventana)
cantidad_entry.config(bg="#C0C0C0")
cantidad_entry.grid(row=0, column=1, padx=5, pady=5)

porcentaje_label = tk.Label(ventana, text="Porcentaje:")
porcentaje_label.config(bg = "#D3D3D3")
porcentaje_label.grid(row=1, column=0, padx=5, pady=5)

porcentaje_entry = tk.Entry(ventana)
porcentaje_entry.config(bg="#C0C0C0")
porcentaje_entry.grid(row=1, column=1, padx=5, pady=5)

calcular_button = tk.Button(ventana, text="Calcular", command=calcular_porcentaje)
calcular_button.config(bg = "#778899")
calcular_button.place(x=100, y=120, width=60, height=30)

resultado_label = tk.Label(ventana, text="El resultado es: ")
resultado_label.config(bg = "#D3D3D3")
resultado_label.place(x=20, y=75, width=220, height=30)

limpiar_button = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
limpiar_button.config(bg = "#778899")
limpiar_button.place(x=170, y=120, width=60, height=30)

# Configurar el foco inicial en el campo de cantidad
cantidad_entry.focus()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
