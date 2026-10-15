"""Gaia DR4 epoch-astrometry helpers used by the CASTY notebooks.

The modules here are vendored, unmodified apart from import paths, from
``gaia-dr4-explorer`` (src/gaia_dr4_explorer), (c) 2026 Vasily Belokurov,
MIT licence; see ``casty/LICENSE``.  Only the code the notebooks need is kept:

- ``fitting``    <- products/astrometry/fitting.py
- ``normalize``  <- products/astrometry/normalize.py
- ``times``      <- products/astrometry/times.py
- ``schema``     <- products/astrometry/schema.py
- ``provenance`` <- domain/provenance.py
"""

#: Version of gaia-dr4-explorer the modules were vendored from.  normalize.py
#: records it in provenance under the "gaia_dr4_explorer" key.
__version__ = "0.1.0.dev0"

__all__ = ["__version__"]
