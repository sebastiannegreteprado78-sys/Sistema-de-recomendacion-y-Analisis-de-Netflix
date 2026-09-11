"""Pregunta 2: perfil de preferencias por genero y titulo."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

CATALOGO_GENEROS = {
    "Stranger Things": "Ciencia Ficcion",
    "The Matrix": "Accion",
    "The Office": "Comedia",
    "El Viaje de Chihiro": "Animacion",
    "Dark": "Ciencia Ficcion",
    "Black Mirror": "Ciencia Ficcion",
}


def extraer_nombre_programa(titulo: str) -> str:
    """Elimina temporada y capitulo para obtener el titulo base."""
    return titulo.split(":")[0].strip()


def enriquecer_con_generos(actividad: pd.DataFrame) -> pd.DataFrame:
    """Anade titulo base y genero al historial."""
    resultado = actividad.copy()
    resultado["Programa"] = resultado["Title"].map(extraer_nombre_programa)
    resultado["Genre"] = resultado["Programa"].map(CATALOGO_GENEROS)
    return resultado


def calcular_top_generos(actividad: pd.DataFrame, por_titulo_unico: bool = False) -> pd.Series:
    """Cuenta exposicion por episodio o diversidad por programa distinto."""
    base = actividad.drop_duplicates("Programa") if por_titulo_unico else actividad
    return base["Genre"].dropna().value_counts()


def graficar_preferencias(actividad: pd.DataFrame, ruta_salida: str | Path) -> None:
    """Guarda un grafico combinado de titulos y generos mas consumidos."""
    fig, ejes = plt.subplots(1, 2, figsize=(14, 5))
    actividad["Programa"].value_counts().sort_values().plot.barh(ax=ejes[0], color="#2a9d8f")
    ejes[0].set_title("Reproducciones por programa")
    ejes[0].set_xlabel("Reproducciones")
    ejes[0].set_ylabel("")
    calcular_top_generos(actividad).sort_values().plot.barh(ax=ejes[1], color="#e76f51")
    ejes[1].set_title("Generos por exposicion")
    ejes[1].set_xlabel("Reproducciones")
    ejes[1].set_ylabel("")
    fig.tight_layout()
    fig.savefig(ruta_salida)
    plt.close(fig)
