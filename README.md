# LuisAntonio_HernandezJardinez_proyectoM3
Simulación de la Máquina de Galton
Descripción del Proyecto
Este programa simula el comportamiento de una Máquina de Galton, un experimento diseñado por Francis Galton para ilustrar la distribución normal a través de eventos aleatorios.

El sistema consiste en 3000 canicas que caen a través de 12 niveles de obstáculos. En cada nivel, la canica puede moverse a la izquierda o a la derecha con igual probabilidad. Al final, los resultados se presentan en un histograma que muestra la cantidad de canicas en cada contenedor.

¿Cómo se hizo el programa?
El programa está estructurado en dos funciones principales:

#simular_caida_canicas(num_canicas=3000, niveles=12)
Simula el proceso de caída de las canicas.
Usa random.choice([0,1]) para decidir si la canica se mueve a la izquierda (0) o a la derecha (1).
Registra el número de canicas que terminan en cada contenedor.
#graficar_histograma(contenedores)
Utiliza matplotlib para representar los resultados en un histograma.
Se añaden etiquetas para los ejes y un título.
# Ejecución del programa
El código se ejecuta en la función principal:
if __name__ == "__main__":
    resultados = simular_caida_canicas()
    graficar_histograma(resultados)
= Reflexiones sobre el Bootcamp
A lo largo de este bootcamp, hemos adquirido conocimientos valiosos en programación con Python. Algunas reflexiones importantes:

% Entender estructuras de control: Implementar bucles y listas en un problema real mejoró mi lógica de programación.

% Simulación de procesos físicos: Fue interesante ver cómo la aleatoriedad puede modelar un fenómeno estadístico como la distribución normal.

%Visualización de datos: Aprender matplotlib permitió representar la información de manera clara y efectiva.

%Pensamiento lógico y resolución de problemas: El proyecto ayudó a aplicar lo aprendido en condiciones reales, fortaleciendo el análisis de problemas complejos.
