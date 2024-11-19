#Notas

Dataset balanceado (buen muestreo)

Para saber si es aprendizaje supervisado o no supervisado:
- etiquetas de salida? si = supervisado, no = no supervisado
- resultado es discreto (SI/NO) o continuo (regresión)


# Respuestas

## Supuesto 1

### Hospital

En este caso, el paradigma central podría ser el aprendizaje supervisado porque se dispone de un conjunto de más de 100 mil casos estudiados y etiquetados aunque se desconoce la distribución que siguen los casos estudiados (sesos de rangos de edad, etc.).

De cada caso estudiado se conoce:

- Edad.
- Número de embarazos.
- Nivel de glucosa.
- Presión sanguínea.
- Pliegue cutáneo.
- Insulina.
- Indice de masa corporal.
- Historial familiar de diabetes.
- Si tiene diabetes o no.

El objetivo del modelo es aprender a:

- Detectar la diabetes en mujeres.
- Aprender a predecir nuevas entradas basandose en el patrón aprendido a partir de los datos etiquetados.

El conjunto total de datos debe separarse en: datos preprocesado, validación y pruebas. Aquí es importante elegir un buen muestreo para cada una de ellas: que tengan diferentes rangos de edad, género, etc. para evitar sesgos.

## Supuesto 2

### Inmobiliaria

En este caso, el paradigma central es el aprendizaje supervisado porque se dispone de un conjunto de más de 200 mil fichas de inmuebles vendidos en el último año en terreno nacional, donde los inmuebles están clasificados indicando:

- Metros cuadrados habitables.
- Número de habitaciones.
- Categoría de inmueble (piso, casa, adosado).
- Código postal donde se encuentra el inmueble.
- Valor según catastro.
- Año de construcción.
- Número de reformas realizadas hasta la fecha.
- Precio de venta.

Teniendo en cuenta todas estas características y que los datos etiquetados son recientes, el modelo podría aprender a predecir el precio de venta de un inmueble.

El conjunto total de datos debe separarse en: datos preprocesado, validación y pruebas.

## Supuesto 3

### Fraudes bancarios

OBJETIVO: Obtener un modelo que ayude a detectar posibles usos fraudulentos en tarjetas de crédito.

Se dispone de una base de datos con más de 2 millones de transacciones en el periodo de los últimos 9 meses.

ANÁLISIS: De cada transacción se conocen diferentes etiquetas pero no se menciona si estas transacciones cuentan con una etiqueta que las clasifique en fraudulentas sí/no.

SUPUESTO 1: Si se dispone de dicha etiqueta, el problema es de clasificación (operación fraudulenta/no fraudulenta). El objetivo sería predefir la categoría: fraude o no fraude. Aplicaría el paradigma del aprendizaje supervisado.

SUPUESTO 2: Si no se dispone de dicha etiqueta, el problema pasa a ser un problema de detección de operación anómala, que se salga de la distribución estandar de datos. El objetivo sería identificar los patrones comunes en los datos y detectar transacciones que no se ajustan. Aplicaría el paradigma del aprendizaje no supervisado.

## Supuesto 4

### Cámara móvil reconocimiento facial

En este caso, el paradigma central es el aprendizaje supervisado porque se dispone de un conjunto de más de 2 millones de datos etiquetados, donde las imágenes están clasificadas indicando:

- La presencia o ausencia de rostros.
- Las coordenadas de los rostros en la imagen (bounding boxes u otros formatos).

El objetivo del modelo es aprender a:

- Detectar automáticamente los rostros en las imágenes.
- Predecir las ubicaciones (coordenadas) de los rostros.

Los modelos de detección facial se basan en redes neuronales convolucionales (CNNs) por lo que el aprendizaje profundo sería otro paradigma secundario en este caso.

## Supuesto 5

### Imágenes de dígitos escritos a mano

El aprendizaje es no supervisado ya que no se menciona que el conjunto de imágenes de que se dispone tenga también las respuestas.

## Supuesto 6

### Tweets

Aprendizaje supervisado.

Datos etiquetados.

Problema de clasificación: positivo/negativo/neutral.

## Supuesto 7

### Viviendas

## Supuesto 8

### Flores

***Clasificación, tenemos un numero limitado de posibles clases de flores***
esto importa porque en función de que sea un problema u otro aplicas un algoritmo y otro y puedes llegar a un resultado absurdo


## Supuesto 9

### Diagnóstico médico

## Supuesto 10

### Aerolinea

## Supuesto 11

### Ciberataques

OBJETIVO: Detectar ciberataques a la red de nuestra empresa.

El conjunto de datos sería tráfico de red, con características como direcciones IP, puertos, duración de la sesión, cantidad de datos transferidos, etc.

De cada transacción se conocen diferentes etiquetas pero no se menciona si ese tráfico cuenta con una etiqueta que lo clasifique en ciberataques sí/no.

SUPUESTO 1: Si se dispone de dicha etiqueta, el problema es de clasificación (ciberataque/no ciberataque). El objetivo sería predefir la categoría: ciberataque o no ciberataque. Aplicaría el paradigma del aprendizaje supervisado.

SUPUESTO 2: Si no se dispone de dicha etiqueta, el problema pasa a ser un problema de detección de tráfico anómalo, que se salga de la distribución estandar de datos. El objetivo sería identificar los patrones comunes en los datos y detectar el tráfico que no se ajusta a esos patrones. Aplicaría el paradigma del aprendizaje no supervisado.

## Supuesto 12

### Filtro spam

Aprendizaje supervisado.

Datos etiquetados.

Problema de clasificación: spam/no spam.
