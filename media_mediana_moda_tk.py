from tkinter import Tk, Label, Text, Button, IntVar
from tkinter import ttk
import random

class MediaMedianaModaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de la media, mediana y moda")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

        # Variable para almacenar los números aleatorios
        self.numeros = []

        # Título
        self.title_label = Label(root, text="Cálculo de la media, mediana y moda", font=("Arial", 14))
        self.title_label.grid(row=0, column=1, pady=10)

        # Sección de números aleatorios generados
        self.label_generados = Label(root, text="Números aleatorios generados:")
        self.label_generados.grid(row=1, column=0, padx=10)

        self.numeros_generados_text = Text(root, width=30, height=10, wrap="none")
        self.numeros_generados_text.grid(row=2, column=0, padx=10)
        self.numeros_generados_text.config(state="disabled")  # Deshabilitar edición

        # Sección para elegir cuántos números generar
        self.label_cantidad = Label(root, text="¿Cuántos números aleatorios?")
        self.label_cantidad.grid(row=1, column=1, padx=10)

        self.num_values = IntVar()
        self.combo = ttk.Combobox(root, textvariable=self.num_values, width=5)
        self.combo['values'] = list(range(2, 501))  # Rango de 2 a 100
        self.combo.bind("<<ComboboxSelected>>", self.on_combo_select)  # Acción cuando se selecciona una opción
        self.combo.grid(row=2, column=1, padx=10)

        # Sección de números ordenados
        self.label_ordenados = Label(root, text="Números aleatorios ORDENADOS:")
        self.label_ordenados.grid(row=1, column=2, padx=10)

        self.numeros_ordenados_text = Text(root, width=30, height=10, wrap="none")
        self.numeros_ordenados_text.grid(row=2, column=2, padx=10)
        self.numeros_ordenados_text.config(state="disabled")  # Deshabilitar edición

        # Botones para calcular Media, Mediana y Moda
        self.btn_media = Button(root, text="Calcular Media", command=self.calcular_media, font=("Arial", 12), bg="lightblue", state="disabled")
        self.btn_media.grid(row=3, column=0, pady=10)

        self.btn_mediana = Button(root, text="Calcular Mediana", command=self.calcular_mediana, font=("Arial", 12), bg="lightblue", state="disabled")
        self.btn_mediana.grid(row=3, column=1, pady=10)

        self.btn_moda = Button(root, text="Calcular Moda", command=self.calcular_moda, font=("Arial", 12), bg="lightblue", state="disabled")
        self.btn_moda.grid(row=3, column=2, pady=10)

        # Etiquetas para mostrar resultados de Media, Mediana y Moda
        self.media_result = Label(root, text="", font=("Arial", 18), fg="red", bg="white", width=10)
        self.media_result.grid(row=4, column=0, pady=10)

        self.mediana_result = Label(root, text="", font=("Arial", 18), fg="red", bg="white", width=10)
        self.mediana_result.grid(row=4, column=1, pady=10)

        self.moda_result = Label(root, text="", font=("Arial", 18), fg="red", bg="white", width=15)
        self.moda_result.grid(row=4, column=2, pady=10)

        # Etiqueta para mostrar cuántas veces se repite la moda
        self.moda_frecuencia = Label(root, text="", font=("Arial", 12), fg="blue", bg="white")
        self.moda_frecuencia.grid(row=5, column=2, pady=5)

        # Botón para limpiar todo
        self.btn_limpiar = Button(root, text="Limpiar", command=self.limpiar, font=("Arial", 12), bg="lightcoral")
        self.btn_limpiar.grid(row=6, column=1, pady=10)

    def on_combo_select(self, event):
        self.generar_numeros()

    def generar_numeros(self):
        cantidad = self.num_values.get()
        if cantidad > 0:
            self.numeros = []
            for _ in range(cantidad):
                self.numeros.append(random.randint(1, 500))
            
            self.numeros_generados_text.config(state="normal")  # Habilitar solo para escribir
            self.numeros_ordenados_text.config(state="normal")  # Habilitar solo para escribir
            self.numeros_generados_text.delete(1.0, "end")
            self.numeros_ordenados_text.delete(1.0, "end")

            # Mostrar números generados en formato de tabla (10 columnas por fila)
            self.mostrar_numeros_en_tabla(self.numeros, self.numeros_generados_text)

            # Limpiar la sección de números ordenados (se llenará al calcular la mediana)
            self.numeros_ordenados_text.insert("end", "")
            self.numeros_generados_text.config(state="disabled")
            self.numeros_ordenados_text.config(state="disabled")

            # Habilitar los botones de Media, Mediana y Moda
            self.habilitar_botones(True)

    def mostrar_numeros_en_tabla(self, numeros, text_widget):
        columnas = 10  # 10 columnas por fila
        filas = []
        for i in range(0, len(numeros), columnas):
            filas.append(numeros[i:i + columnas])
        for fila in filas:
            text_widget.insert("end", " ".join(f"{num:2}" for num in fila) + "\n")

    def calcular_media(self):
        suma = 0
        for num in self.numeros:
            suma += num
        media = suma / len(self.numeros)
        self.media_result.config(text=f"{media:.2f}")

    def calcular_mediana(self):
        # Ordenar manualmente los números solo para la mediana
        self.numeros_ordenados = []
        for num in self.numeros:
            inserted = False
            for i in range(len(self.numeros_ordenados)):
                if num < self.numeros_ordenados[i]:
                    self.numeros_ordenados.insert(i, num)
                    inserted = True
                    break
            if not inserted:
                self.numeros_ordenados.append(num)

        # Mostrar números ordenados
        self.numeros_ordenados_text.config(state="normal")
        self.numeros_ordenados_text.delete(1.0, "end")
        self.mostrar_numeros_en_tabla(self.numeros_ordenados, self.numeros_ordenados_text)
        self.numeros_ordenados_text.config(state="disabled")

        # Calcular mediana
        n = len(self.numeros_ordenados)
        if n % 2 == 0:
            mediana = (self.numeros_ordenados[n // 2 - 1] + self.numeros_ordenados[n // 2]) / 2
        else:
            mediana = self.numeros_ordenados[n // 2]
        self.mediana_result.config(text=f"{mediana:.2f}")

    def calcular_moda(self):
        contador = {}
        for num in self.numeros:
            if num in contador:
                contador[num] += 1
            else:
                contador[num] = 1
        
        # Encontrar la frecuencia máxima
        max_frecuencia = max(contador.values())
        
        # Buscar todas las modas (números que se repiten con la frecuencia máxima)
        modas = [num for num, freq in contador.items() if freq == max_frecuencia]
        
        # Si solo hay una moda, mostrarla. Si hay más de una, indicar que no hay moda
        if len(modas) == 1:
            self.moda_result.config(text=str(modas[0]))
            self.moda_frecuencia.config(text=f"Se repitió {max_frecuencia} veces")
        else:
            self.moda_result.config(text="N/A")
            self.moda_frecuencia.config(text="No hay moda")
        
    def limpiar(self):
        self.numeros_generados_text.config(state="normal")  # Habilitar solo para limpiar
        self.numeros_ordenados_text.config(state="normal")  # Habilitar solo para limpiar
        self.numeros_generados_text.delete(1.0, "end")
        self.numeros_ordenados_text.delete(1.0, "end")
        self.media_result.config(text="")
        self.mediana_result.config(text="")
        self.moda_result.config(text="")
        self.moda_frecuencia.config(text="")
        self.numeros = []
        self.habilitar_botones(False)

    def habilitar_botones(self, estado):
        self.btn_media.config(state="normal" if estado else "disabled")
        self.btn_mediana.config(state="normal" if estado else "disabled")
        self.btn_moda.config(state="normal" if estado else "disabled")

# Configurar la aplicación
root = Tk()
app = MediaMedianaModaApp(root)
root.mainloop()
