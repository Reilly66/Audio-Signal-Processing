import os
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_TIME = 0.1
SAMPLE_RATE = 15000
FIGURES_DIR = os.path.join(os.path.dirname(__file__), 'report', 'figures')

def generate_signal(t):
    amps = np.array([0.67, 0.74, 1])
    freqs = np.array([320, 240, 160])
    phase = np.random.rand(len(amps)) * 2 * np.pi
    x = np.zeros_like(t)
    for amp, freq, phi in zip(amps, freqs, phase):
        x += amp * np.sin(2 * np.pi * freq * t + phi)
    return x

def plot_signal(t, x):
    plt.plot(t, x)
    plt.title('Generated Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.savefig(os.path.join(FIGURES_DIR, 'signal.png'), dpi=150, bbox_inches='tight')
    plt.show()

def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = np.arange(N).reshape(-1, 1)
    X = np.sum(x * np.exp(-2j * np.pi * k * n / N), axis=1)
    return X
    

def plot_spectrum(X, sr):
    N = len(X)
    freqs = np.arange(N) * sr / N
    magnitude = np.abs(X) / N
    plt.bar(freqs[:N // 2], magnitude[:N // 2], width=sr / N)
    threshold = np.max(magnitude[:N // 2]) * 0.01
    significant = freqs[:N // 2][magnitude[:N // 2] > threshold]
    plt.xlim(0, significant[-1] * 1.5)
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid()
    plt.savefig(os.path.join(FIGURES_DIR, 'spectrum.png'), dpi=150, bbox_inches='tight')
    plt.show()


def main():
    os.makedirs(FIGURES_DIR, exist_ok=True)
    t = np.linspace(0, SAMPLE_TIME, int(SAMPLE_TIME * SAMPLE_RATE))
    x = generate_signal(t)
    plot_signal(t, x)
    X = DFT(x)
    plot_spectrum(X, SAMPLE_RATE)


if __name__ == '__main__':
    main()
