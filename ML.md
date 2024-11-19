# Machine Learning Intro

## AI. Artificial Inteligence

Capacidad de las máquinas para simular y realizar tareas que normalmente requieren inteligencia humana, como el aprendizaje, el razonamiento, la resolución de problemas, el reconocimiento de patrones y la toma de decisiones.

## ML. Machine Learning

IA tradicional: los programas se diseñan con reglas explícitas => 
datos + reglas => programción clásica => resultados
x + f (funcion) => y
ML: construye modelos aprendiendo a partir de datos, cuantos más datos se le proporcionan, más aprende y mejor es el modelo que construye.

## DL. Deep Learning

Subdisciplina del ML, arquitecturas de redes neuronales (multiples capas). Posible gracias al incremento en la capacidad de procesamiento del hardware (GPGPU).

## Modelos

Contruccion conceptual simplificada de una realidad más compleja.
Uso de la probabilidad para reducir intertidumbre.

## Paradigmas de aprendizaje

### Aprendizaje Supervisado. Supervised Learning

El modelo se entrena utilizando un conjunto de datos etiquetado (recibe la relación correcta entre inputs y outputs).

Objetivo del modelo: aprender a predecir o clasificar nuevas entradas basandose en el patrón aprendido a partir de los datos etiquetados.

Ejemplos: clasificación (correo spam) y regresión (predecir si una persona va a sufrir depresión a partir de su cuenta de Instagram, predecir precio de una casa en función de sus características).

### Aprendizaje No Supervisado. Unsupervised Learning

El modelo consigue producir conocimiento únicamente con los inputs.

Objetivo del modelo: Encontrar patrones de similitud entre los datos de entrada sin guía externa sobre las respuestas correctas.

Ventaja: Conjuntos de datos para entrenar son menos costosos.

Métodos más comunes: clusterización (agrupamiento) de datos según similitudes (segmentación de mercado) y reducción de dimensionalidad, simplificar los datos reduciendo variables manteniento la mayor información posible (análisis de los componentes principales = PCA).

### Aprendizaje Reforzado. Reinforcement Learning

El modelo recibe retroalimentación del entorno en forma de recompensas/penalizaciones por las acciones que realiza.

Relación agente -> entorno

Conceptos:

1. Agente (Agent) = Es la entidad que toma decisiones en el entorno. Puede ser, por ejemplo, un robot, un software
2. Entorno (Environment) = Responde a las acciones del agente y le proporciona retroalimentación. (robot/habitación, videojuego/virtual)
3. Estado (State) = representación de la situación actual del agente en el entorno (ajedrez/la disposición de las piezas en tablero)
4. Acción (Action) = Decisiones que el agente puede tomar en un estado determinado (mover pieza, saltar, etc)
5. Recompensa (Reward) = Señal después de realizar acción. Puede ser positiva o negativa.
6. Política (Policy) = estrategia que sigue el agente en la toma de decisiones. Puede ser determinista (siempre elige la misma acción en tal mismom estado) o probabilistica (elegir entre varias acciones con probabilidad)
7. Valor (Value) = Es una estimación del retorno esperado (recompensas acumuladas) que se puede obtener a partir de un estado dado, siguiendo una política determinada.
8. Función de valor (Value Function): Estima el valor de un estado, es decir, cuánta recompensa se puede esperar obtener a partir de ese estado.

Ejemplo: el problema de Q-learning, juegos, robótica, automóviles autónomos, publicidad online, gestión de inventarios.

#NOTAS
variables de salida, son conjuntos discretos o continuos?
discreto => clasificación
continuos => regresión

ejemplo diabetes, np load_dataset, puedes visualizarlo ocomo dataset pandas
ojo porque si es si/no, si es una etiqueta discresión


el dataset,el numero de datos depende de la varianza, en flores, o efecto de un medicamento en personas (vigo, amigos)
-muestreo
-distribución
-sesgo

correlación y causalidad, no es lo mismo puede ser que ambas cosas sean correladas por la misma causa
correlación (features, variable de entrada) => muy predictor

ejemplo de pétalos ya muestra colores clasificados sin haber entrenado el modelo

si coges uno de 

IMPORTANTE
algoritmo de regresión logistica. es de clasificación no de regresión
hace regresión sobre la probabilidad de que sea una y otra
es regresión en cuanto a que mide probabilidad pero la finalidad es clasificar, categorizar 
la forma de la regr logítica es una S





no supervisado:
clusterizado 
reducción dimensionalidad: ver las caracteristicas que más ponderan. simplificar el modelo. aprendizaje no suèrvsado en fases de preprocesado.
feature engineering.



