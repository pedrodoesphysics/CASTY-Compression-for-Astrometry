# CASTY-Compression-for-Astrometry
A collection of notes and script in relation to the project of optimally compressing astrometric epoch data, for the purpose of internal collaboration.

## Setup

The repository is self-contained: the Gaia DR4 helpers the notebooks use live in
`casty/` (vendored from `gaia-dr4-explorer`, MIT, see `casty/LICENSE`), and the
prerelease epoch-astrometry VOTable is in `prerelease_DR4_test/`.

```bash
pip install -r requirements.txt
```

Run the notebooks from the repository root so `import casty` and the relative
data path resolve.
