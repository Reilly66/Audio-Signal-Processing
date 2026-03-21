# Bayesian Audio Signal Processing

Spectral-domain Bayesian audio denoising and source separation using Wiener filtering with learned priors.

## Overview

This project implements a Bayesian approach to audio signal processing in the STFT (Short-Time Fourier Transform) domain. The core technique is Wiener filtering, where signal and noise power spectral densities (PSDs) are estimated using configurable prior models — from simple stationary noise profiles to learned NMF-based spectral templates and variational inference.

## Features

- **Wiener filtering** — optimal linear filtering in the spectral domain using PSD estimates
- **Multiple noise priors** — stationary, adaptive (minimum statistics), and NMF-based learned priors
- **Variational inference** — full Bayesian treatment with uncertainty estimates via variational EM over latent spectral models
- **Source separation** — multi-source Wiener filtering for separating mixed audio signals
- **CLI and library** — usable as a Python library or command-line tool

## Approach

The Wiener filter gain at each time-frequency bin is:

```
G(f, t) = P_signal(f, t) / (P_signal(f, t) + P_noise(f, t))
```

The Bayesian aspect lies in how `P_signal` and `P_noise` are estimated:

| Prior Model | Description |
|---|---|
| **Stationary** | Noise PSD estimated from a noise-only segment, constant over time |
| **Adaptive** | Tracks non-stationary noise using minimum statistics |
| **NMF** | Learns spectral basis matrices from training data; infers activations at test time |
| **Variational** | Gamma priors over NMF activations with variational EM inference, providing posterior uncertainty |

## Installation

```bash
pip install -e ".[dev]"
```

### Dependencies

- Python >= 3.10
- NumPy, SciPy, SoundFile

## Usage

### Library

```python
import bayesaudio

# Denoise with a stationary noise prior
cleaned = bayesaudio.denoise(signal, sr, noise_prior="stationary")

# Separate a mixture into 2 sources using NMF priors
sources = bayesaudio.separate(signal, sr, n_sources=2)
```

### CLI

```bash
bayesaudio denoise input.wav output.wav --prior stationary --noise-frames 20
bayesaudio separate input.wav output_dir/ --n-sources 2
```

## Project Structure

```
bayesaudio/
├── stft.py          # STFT / iSTFT transform layer
├── wiener.py        # Wiener filter gain computation
├── priors.py        # Noise/signal prior models
├── variational.py   # Variational inference engine
├── denoise.py       # Denoising pipeline
├── separate.py      # Source separation pipeline
├── io.py            # Audio file I/O
└── cli.py           # Command-line interface
```

## License

MIT
