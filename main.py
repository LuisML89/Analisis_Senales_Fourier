
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
