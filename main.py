
import numpy as np
import matplotlib.pyplot as plt

# Actividad: Analisis de Senales y Sistemas
# Senal senoidal en el dominio del tiempo

# Parametros de la senal
frecuencia = 5  # Frecuencia en Hz
amplitud = 1    # Amplitud de la senal
tiempo = np.linspace(0, 1, 1000, endpoint=False)

# Generar la senal senoidal
senal = amplitud * np.sin(2 * np.pi * frecuencia * tiempo)

# Representar la senal en el dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(tiempo, senal, color="blue", label="Senal senoidal")

plt.title("Senal senoidal en el dominio del tiempo")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()

# Mostrar la grafica
plt.show()

# Transformada de Fourier de la senal senoidal

# Frecuencia de muestreo y numero de muestras
frecuencia_muestreo = 1000
N = len(senal)

# Calcular la Transformada Rapida de Fourier
transformada = np.fft.fft(senal)

# Obtener las frecuencias correspondientes
frecuencias = np.fft.fftfreq(N, d=1/frecuencia_muestreo)

# Centrar las frecuencias y el espectro
frecuencias = np.fft.fftshift(frecuencias)
transformada = np.fft.fftshift(transformada)

# Calcular magnitud normalizada y fase
magnitud = np.abs(transformada) / N
fase = np.angle(transformada)

# Evitar mostrar fases donde la magnitud es casi cero
fase[magnitud < 1e-10] = 0

# Crear las graficas del espectro
plt.figure(figsize=(10, 7))

plt.subplot(2, 1, 1)
plt.plot(frecuencias, magnitud, color="red")
plt.title("Espectro de magnitud de la senal senoidal")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.xlim(-20, 20)
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(frecuencias, fase, color="green")
plt.title("Espectro de fase de la senal senoidal")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (radianes)")
plt.xlim(-20, 20)
plt.grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# SEGUNDA SENAL: PULSO RECTANGULAR
# ==========================================

# Crear un pulso rectangular de 0.2 segundos
pulso = np.where(
    (tiempo >= 0.4) & (tiempo < 0.6), 1, 0
)

# Calcular la Transformada de Fourier
fft_pulso = np.fft.fft(pulso)
fft_pulso = np.fft.fftshift(fft_pulso)

# Calcular magnitud y fase
magnitud_pulso = np.abs(fft_pulso) / N
fase_pulso = np.angle(fft_pulso)

# Evitar fases en componentes casi nulas
fase_pulso[magnitud_pulso < 1e-10] = 0

# Crear las tres graficas
plt.figure(figsize=(10, 9))

# Grafica en el dominio del tiempo
plt.subplot(3, 1, 1)
plt.plot(tiempo, pulso, color="blue")
plt.title("Pulso rectangular - Dominio del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

# Espectro de magnitud
plt.subplot(3, 1, 2)
plt.plot(frecuencias, magnitud_pulso, color="red")
plt.title("Pulso rectangular - Espectro de magnitud")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.xlim(-50, 50)
plt.grid(True)

# Espectro de fase
plt.subplot(3, 1, 3)
plt.plot(frecuencias, fase_pulso, color="green")
plt.title("Pulso rectangular - Espectro de fase")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (radianes)")
plt.xlim(-50, 50)
plt.grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# TERCERA SENAL: FUNCION ESCALON
# ==========================================

# Crear la funcion escalon en t = 0.5 segundos
escalon = np.where(tiempo >= 0.5, 1, 0)

# Calcular la Transformada de Fourier
fft_escalon = np.fft.fft(escalon)
fft_escalon = np.fft.fftshift(fft_escalon)

# Calcular magnitud y fase
magnitud_escalon = np.abs(fft_escalon) / N
fase_escalon = np.angle(fft_escalon)

# Evitar fases en componentes casi nulas
fase_escalon[magnitud_escalon < 1e-10] = 0

# Crear las tres graficas
plt.figure(figsize=(10, 9))

# Dominio del tiempo
plt.subplot(3, 1, 1)
plt.plot(tiempo, escalon, color="blue")
plt.title("Funcion escalon - Dominio del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

# Espectro de magnitud
plt.subplot(3, 1, 2)
plt.plot(frecuencias, magnitud_escalon, color="red")
plt.title("Funcion escalon - Espectro de magnitud")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.xlim(-50, 50)
plt.grid(True)

# Espectro de fase
plt.subplot(3, 1, 3)
plt.plot(frecuencias, fase_escalon, color="green")
plt.title("Funcion escalon - Espectro de fase")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (radianes)")
plt.xlim(-50, 50)
plt.grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# PROPIEDAD 1: LINEALIDAD DE FOURIER
# ==========================================

# Crear dos senales senoidales
senal_1 = np.sin(2 * np.pi * 5 * tiempo)
senal_2 = np.sin(2 * np.pi * 10 * tiempo)

# Constantes de combinacion
a = 2
b = 3

# Combinar las senales en el dominio del tiempo
senal_combinada = a * senal_1 + b * senal_2

# Calcular la FFT de la senal combinada
fft_combinada = np.fft.fft(senal_combinada)

# Calcular las FFT individuales y combinarlas
fft_lineal = (
    a * np.fft.fft(senal_1)
    + b * np.fft.fft(senal_2)
)

# Comprobar la propiedad de linealidad
error = np.max(np.abs(fft_combinada - fft_lineal))

print("PROPIEDAD DE LINEALIDAD")
print("Error maximo:", error)

# Preparar los espectros para visualizarlos
fft_combinada_centrada = np.fft.fftshift(fft_combinada)
fft_lineal_centrada = np.fft.fftshift(fft_lineal)

magnitud_combinada = np.abs(fft_combinada_centrada) / N
magnitud_lineal = np.abs(fft_lineal_centrada) / N

# Crear graficas
plt.figure(figsize=(10, 9))

# Senales individuales
plt.subplot(3, 1, 1)
plt.plot(tiempo, senal_1, label="Senal 1: 5 Hz")
plt.plot(tiempo, senal_2, label="Senal 2: 10 Hz")
plt.title("Linealidad - Senales originales")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)

# Senal combinada
plt.subplot(3, 1, 2)
plt.plot(tiempo, senal_combinada, color="purple")
plt.title("Combinacion lineal: 2x1(t) + 3x2(t)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

# Comparacion de transformadas
plt.subplot(3, 1, 3)
plt.plot(
    frecuencias,
    magnitud_combinada,
    color="red",
    linewidth=2,
    label="FFT de la combinacion"
)
plt.plot(
    frecuencias,
    magnitud_lineal,
    color="black",
    linestyle="--",
    label="Combinacion de las FFT"
)

plt.title("Verificacion de la propiedad de linealidad")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.xlim(-20, 20)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# PROPIEDAD 2: DESPLAZAMIENTO TEMPORAL
# ==========================================

# Crear un pulso rectangular original
pulso_original = np.where(
    (tiempo >= 0.2) & (tiempo < 0.4), 1, 0
)

# Desplazar el pulso 0.1 segundos a la derecha
desplazamiento = 0.1

pulso_desplazado = np.where(
    (tiempo >= 0.3) & (tiempo < 0.5), 1, 0
)

# Calcular las transformadas de Fourier
fft_original = np.fft.fft(pulso_original)
fft_desplazado = np.fft.fft(pulso_desplazado)

# Calcular la frecuencia de muestreo
fs = 1 / (tiempo[1] - tiempo[0])

# Calcular el factor de fase
factor_fase = np.exp(
    -1j * 2 * np.pi
    * np.fft.fftfreq(N, d=1/fs)
    * desplazamiento
)

fft_esperada = fft_original * factor_fase

# Comprobar la propiedad
error_desplazamiento = np.max(
    np.abs(fft_desplazado - fft_esperada)
)

print("PROPIEDAD DE DESPLAZAMIENTO TEMPORAL")
print("Error maximo:", error_desplazamiento)

# Centrar los espectros
fft_original_c = np.fft.fftshift(fft_original)
fft_desplazado_c = np.fft.fftshift(fft_desplazado)

magnitud_original = np.abs(fft_original_c) / N
magnitud_desplazada = np.abs(fft_desplazado_c) / N

fase_original = np.angle(fft_original_c)
fase_desplazada = np.angle(fft_desplazado_c)

# Crear graficas
plt.figure(figsize=(10, 10))

# Grafica 1: senales en el tiempo
plt.subplot(3, 1, 1)
plt.plot(tiempo, pulso_original,
         label="Pulso original")
plt.plot(tiempo, pulso_desplazado,
         label="Pulso desplazado 0.1 s",
         linestyle="--")
plt.title("Desplazamiento temporal - Senales")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)

# Grafica 2: comparar magnitudes
plt.subplot(3, 1, 2)
plt.plot(frecuencias, magnitud_original,
         label="Magnitud original", color="blue")
plt.plot(frecuencias, magnitud_desplazada,
         label="Magnitud desplazada",
         color="red", linestyle="--")
plt.title("Comparacion de espectros de magnitud")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.xlim(-30, 30)
plt.legend()
plt.grid(True)

# Grafica 3: comparar fases
plt.subplot(3, 1, 3)

# Mostrar fase solo donde hay magnitud significativa
umbral = 0.005
fase_original[magnitud_original < umbral] = np.nan
fase_desplazada[magnitud_desplazada < umbral] = np.nan

plt.plot(frecuencias, fase_original,
         label="Fase original", color="green")
plt.plot(frecuencias, fase_desplazada,
         label="Fase desplazada",
         color="purple", linestyle="--")
plt.title("Comparacion de espectros de fase")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (radianes)")
plt.xlim(-30, 30)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# PROPIEDAD 3: ESCALAMIENTO EN FRECUENCIA
# ==========================================

# Definir frecuencia original y factor de escala
frecuencia_original = 5
factor_escala = 2

# Crear señal original de 5 Hz
senal_original_escala = np.sin(
    2 * np.pi * frecuencia_original * tiempo
)

# Crear señal escalada de 10 Hz
senal_escalada = np.sin(
    2 * np.pi * frecuencia_original
    * factor_escala * tiempo
)

# Calcular las transformadas de Fourier
fft_original_escala = np.fft.fft(
    senal_original_escala
)

fft_escalada = np.fft.fft(
    senal_escalada
)

# Centrar los espectros
fft_original_escala = np.fft.fftshift(
    fft_original_escala
)

fft_escalada = np.fft.fftshift(
    fft_escalada
)

# Calcular las magnitudes normalizadas
magnitud_original_escala = (
    np.abs(fft_original_escala) / N
)

magnitud_escalada = (
    np.abs(fft_escalada) / N
)

# Verificar las frecuencias principales
frecuencia_pico_original = frecuencias[
    np.argmax(magnitud_original_escala[
        frecuencias >= 0
    ]) + np.where(frecuencias >= 0)[0][0]
]

frecuencia_pico_escalada = frecuencias[
    np.argmax(magnitud_escalada[
        frecuencias >= 0
    ]) + np.where(frecuencias >= 0)[0][0]
]

print("PROPIEDAD DE ESCALAMIENTO")
print("Frecuencia original:",
      frecuencia_pico_original, "Hz")
print("Frecuencia escalada:",
      frecuencia_pico_escalada, "Hz")

# Crear graficas
plt.figure(figsize=(10, 9))

# Grafica 1: señal original
plt.subplot(3, 1, 1)
plt.plot(tiempo, senal_original_escala,
         color="blue")
plt.title("Señal original de 5 Hz")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

# Grafica 2: señal escalada
plt.subplot(3, 1, 2)
plt.plot(tiempo, senal_escalada,
         color="purple")
plt.title("Señal escalada de 10 Hz")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

# Grafica 3: comparación de espectros
plt.subplot(3, 1, 3)
plt.plot(frecuencias, magnitud_original_escala,
         color="blue",
         label="Original: 5 Hz")
plt.plot(frecuencias, magnitud_escalada,
         color="red", linestyle="--",
         label="Escalada: 10 Hz")

plt.title("Propiedad de escalamiento en frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud normalizada")
plt.xlim(-20, 20)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
