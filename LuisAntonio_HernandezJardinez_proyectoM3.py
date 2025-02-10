import random
import matplotlib.pyplot as plt

# Función para simular la caída de las canicas en la máquina de Galton
def simular_caida_canicas(num_canicas=3000, niveles=12):
    contenedores = [0] * (niveles + 1)  # Se crea una lista para almacenar las canicas en cada contenedor
    
    for _ in range(num_canicas):
        posicion = 0  # Comenzamos desde el centro
        for _ in range(niveles):
            posicion += random.choice([0, 1])  # 0 representa izquierda, 1 representa derecha
        contenedores[posicion] += 1  # Se incrementa el contenedor donde cayó la canica

    return contenedores

# Función para graficar los resultados en un histograma
def graficar_histograma(contenedores):
    plt.bar(range(len(contenedores)), contenedores, color='blue', edgecolor='black')
    plt.xlabel("Número de contenedor")
    plt.ylabel("Cantidad de canicas")
    plt.title("Simulación de la Máquina de Galton")
    plt.show()

# Ejecución del programa
if __name__ == "__main__":
    resultados = simular_caida_canicas()
    graficar_histograma(resultados)
