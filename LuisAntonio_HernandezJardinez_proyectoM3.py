import random
import matplotlib.pyplot as plt

# Función para simular la caída de las canicas en la máquina de Galton
def simular_caida_canicas(num_canicas=3000, niveles=12):
    contenedores = [0] * (niveles + 1)  # Se crean los contenedores

    # Simulación de la caída de las canicas
    for _ in range(num_canicas):
        posicion = 0  # Inicia desde el centro
        for _ in range(niveles):
            posicion += random.choice([0, 1])  # Se mueve aleatoriamente a la izquierda (0) o derecha (1)
        contenedores[posicion] += 1  # Se suma una canica al contenedor final

    return contenedores

# Función para graficar el histograma
def graficar_histograma(contenedores):
    plt.bar(range(len(contenedores)), contenedores, color='blue', edgecolor='black')
    plt.xlabel("Número de contenedor")  # Etiqueta del eje X
    plt.ylabel("Cantidad de canicas")  # Etiqueta del eje Y
    plt.title("Simulación de la Máquina de Galton")  # Título del gráfico
    plt.show()

# Ejecución del programa
if __name__ == "__main__":
    resultados = simular_caida_canicas()  # Ejecuta la simulación
    graficar_histograma(resultados)  # Muestra el histograma

