"""Estilo visual compartido por todos los graficos."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def aplicar_estilo_minimalista() -> None:
    """Configura una apariencia consistente y legible para los graficos."""
    sns.set_theme(style="whitegrid", context="notebook")
    plt.rcParams.update(
        {
            "figure.figsize": (10, 6),
            "axes.titleweight": "bold",
            "axes.titlesize": 15,
            "axes.labelsize": 11,
            "figure.dpi": 110,
            "savefig.bbox": "tight",
        }
    )


def preparar_directorio_salida(directorio: Path) -> Path:
    """Crea el directorio de graficos si no existe y lo devuelve."""
    directorio.mkdir(parents=True, exist_ok=True)
    return directorio
