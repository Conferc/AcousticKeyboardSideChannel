# Import Libraries
import glob
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt


# Method for Plotting FFT's of Key Press and Release Recordings
# Source: https://stackoverflow.com/questions/23377665/python-scipy-fft-wav-files
def f(filename):
    fs_rate, signal = wavfile.read(filename)
    print("Frequency sampling", fs_rate)
    l_audio = len(signal.shape)
    print("Channels", l_audio)
    if l_audio == 2:
        signal = signal.sum(axis=1) / 2
    N = signal.shape[0]
    print("Complete Samplings N", N)
    secs = N / float(fs_rate)
    print("secs", secs)
    Ts = 1.0 / fs_rate  # sampling interval in time
    print("Timestep between samples Ts", Ts)
    t = np.arange(0, secs, Ts)  # time vector as scipy arange field / numpy.ndarray
    FFT = abs(scipy.fft.fft(signal))
    freqs = scipy.fftpack.fftfreq(signal.size, t[1] - t[0])
    p1 = plt.plot(t, signal, "g")  # plotting the signal
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    p2 = plt.plot(freqs, FFT, "r")  # plotting the complete fft spectrum
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Count dbl-sided')


# Create Plot of Key Press Regions
for filepath in glob.glob(r'UnknownSamples\Unknown3\Press?.wav', recursive=True):
    f(filepath)
    print("Press:" + filepath)
    if filepath == r"UnknownSamples\Unknown3\Press5.wav":
        print("Plotting all Key Press graphs!")
        plt.title("Unknown Press 3")
plt.show()  # Show Plot of Key Press Regions

# Create Plot of Key Release Regions
for filepath in glob.glob(r'UnknownSamples\Unknown3\Release?.wav', recursive=True):
    f(filepath)
    print("Release: " + filepath)
    if filepath == r"UnknownSamples\Unknown3\Release5.wav":
        print("Plotting all Key Release Graphs!")
        plt.title("Unknown Release 3")

plt.show()  # Show Plot of Key Release Regions
quit()
