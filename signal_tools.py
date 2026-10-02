import plotly.graph_objects as go
from scipy.fft import fft, fftfreq
import numpy as np

def loadSignalFromCSV(file_path):
    signal = []
    with open(file_path, 'r') as f:
        for line in f:
            signal.append(float(line.strip()))

    print(f"Read {len(signal)} samples from {file_path}")
    return signal


def plotSignal(t, signal):
    fig = go.Figure(
        data=go.Scatter(
            x=t,
            y=signal,
            mode='lines+markers',
            name='Signal',
            marker=dict(size=5)
        )
    )

    fig.update_layout(
        title='Signal',
        xaxis_title='Time (s)',
        yaxis_title='Amplitude',
        xaxis=dict(rangeslider=dict(visible=True)),
        hovermode='x unified'
    )

    return fig


def computeFFT(signal, sample_rate):
    N = len(signal)
    T = 1.0 / sample_rate
    yf = fft(signal)
    xf = fftfreq(N, T)[:N // 2]
    spectrum = np.asarray(yf[:N // 2])
    magnitude = 2.0 / N * np.abs(spectrum)
    return xf, magnitude


def plotFFT(frequencies, fft_magnitude):
    fig = go.Figure(
        data=go.Scatter(
            x=frequencies,
            y=fft_magnitude,
            mode='lines',
            name='Magnitude'
        )
    )

    fig.update_layout(
        title='FFT Spectrum',
        xaxis_title='Frequency (Hz)',
        yaxis_title='Magnitude',
        hovermode='x unified'
    )

    return fig