# IoT Signal Processing: FFT and FIR Filtering

This repository contains a Jupyter Notebook (`fft-example.ipynb`) that demonstrates basic signal processing techniques using Python. The focus is on analyzing and filtering signals, which are common tasks in IoT applications.

## Contents

- **FFT Analysis**:  
    The notebook reads a time-domain signal from `signal-original.csv` and visualizes it. It then performs a Fast Fourier Transform (FFT) to analyze the frequency components of the signal.

- **FIR Filter Design and Application**:  
    A Finite Impulse Response (FIR) filter is designed using an online tool. The filter coefficients are applied to the original signal via convolution to remove unwanted frequencies.

## Installation

### Windows / PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Usage

1. Place your signal data in `signal-original.csv` (one sample per line).
2. Open and run `fft-example.ipynb` in Jupyter Notebook or VS Code.
3. Review the plots and analysis.

## References

- [Online FIR Filter Design Tool](http://t-filter.engineerjs.com/)
