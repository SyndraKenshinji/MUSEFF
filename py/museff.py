# Beat tracking example
import librosa
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf

# 1. Get the file path to an included audio example
filename = 'C:\\Users\\anton\\projetos\\MUSEFF\\audio\\teste.wav'

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)
print('Data loaded')
print(y.shape)

# Param FFT
WINDOW = "boxcar"
N_FFT = 2048
NPERSEG = N_FFT
NOVERLAP = 0

f, t, Zxx = signal.stft(y, sr, nperseg= NPERSEG, noverlap=NOVERLAP, window=WINDOW)
db_zxx = 20*np.log10(np.abs(Zxx))
db_min = np.min(db_zxx)
db_max = np.max(db_zxx)
mask = Zxx

for batata in range(int(len(mask)/2),len(mask)):
    mask[batata] = 1e-10

db_mask = 20*np.log10(np.abs(mask))

_, y_reconstructed = signal.istft(mask, sr, nperseg=NPERSEG, noverlap=NOVERLAP, window=WINDOW)

# Normalizar o sinal reconstruído para evitar estouro
y_reconstructed = y_reconstructed / np.max(np.abs(y_reconstructed))

# Salvar como novo arquivo WAV
sf.write('C:\\Users\\anton\\projetos\\MUSEFF\\audio\\teste_modificado.wav', y_reconstructed, sr)
print("Arquivo salvo com sucesso!")

plt.pcolormesh(t, f,db_mask, vmin=db_min, vmax=db_max, shading='gouraud')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig("bolo.jpeg")


'''
VERSÃO ANTERIOR STFT
print(f"expected length: {y.shape[0]/N_FFT}")
y_f = librosa.stft(y, n_fft=N_FFT, hop_length=HOP_LENGTH)

print(y.shape)
print(y_f.shape)
# fk = sr*k/n
retira a primeira dimensão e armazena as restantes em FK
a primeira dimensão é a dimensão que define a iteração, e as restantes são as armazenadas
k = np.arange(0,y_f.shape[0])'''






