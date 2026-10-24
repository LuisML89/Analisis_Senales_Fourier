# Análisis de Señales y Sistemas mediante la Transformada de Fourier

## Descripción del proyecto

Este proyecto tiene como objetivo analizar diferentes señales mediante Python, utilizando la Transformada Rápida de Fourier (FFT) para estudiar su comportamiento en los dominios del tiempo y de la frecuencia.

Se desarrollaron simulaciones que permiten representar gráficamente las señales, identificar sus componentes de frecuencia y comprobar propiedades fundamentales de la Transformada de Fourier.

## Herramientas utilizadas

- Python 3
- PyCharm
- NumPy
- SciPy
- Matplotlib
- Git y GitHub

## Señales analizadas

**1. Señal senoidal**

Se generó una señal senoidal de 5 Hz y se calculó su Transformada de Fourier. El espectro presenta componentes en las frecuencias de -5 Hz y 5 Hz.

**2. Pulso rectangular**

Se simuló un pulso rectangular para analizar su comportamiento temporal y su espectro de frecuencia, caracterizado por un lóbulo principal y lóbulos secundarios.

**3. Función escalón**

Se representó una función escalón y se calculó su FFT sobre un intervalo finito, observando su contenido de bajas frecuencias.

## Propiedades verificadas

**Linealidad:** Se combinaron dos señales senoidales de 5 Hz y 10 Hz, comprobando que la Transformada de Fourier de su combinación lineal coincide con la combinación de sus transformadas individuales.

**Desplazamiento temporal:** Se desplazó un pulso rectangular 0.1 segundos, verificando que su espectro de magnitud permanece sin cambios mientras que su fase se modifica.

**Escalamiento en frecuencia:** Se compararon señales senoidales de 5 Hz y 10 Hz, comprobando que al comprimir la señal en el tiempo se duplica su frecuencia.

## Resultados

Las simulaciones permitieron comprobar las propiedades estudiadas mediante representaciones gráficas y cálculos numéricos.

En las propiedades de linealidad y desplazamiento temporal se obtuvieron errores numéricos cercanos a cero.

En el escalamiento se identificó el desplazamiento de los componentes espectrales de ±5 Hz a ±10 Hz.

## Ejecución del proyecto

1. Instalar Python 3.
2. Descargar o clonar el repositorio.
3. Instalar las dependencias necesarias:

   `python -m pip install numpy scipy matplotlib`

4. Ejecutar el archivo principal:

   `python main.py`

5. Observar las gráficas generadas y los resultados mostrados en consola.

## Estructura del proyecto

- `main.py`: código principal de las simulaciones.
- `Graficas/`: imágenes de las señales y propiedades verificadas.
- `README.md`: documentación del proyecto.

## Conclusión

El desarrollo de este proyecto permitió comprender la importancia de la Transformada de Fourier en el análisis de señales. Mediante Python fue posible identificar las diferencias entre los dominios del tiempo y de la frecuencia, así como verificar propiedades matemáticas fundamentales.

Los resultados demostraron que las herramientas de programación facilitan la visualización y comprensión de conceptos relacionados con el procesamiento digital de señales.