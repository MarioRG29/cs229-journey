"""Helpers reutilizables (carga de datos, etc.)."""

from pathlib import Path
import pandas as pd


def read_csv_local(path: str | Path, **kwargs) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"No existe el fichero: {p}")
    return pd.read_csv(p, **kwargs)
