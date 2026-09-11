"""Pregunta 4: descubrimiento de titulos poco populares."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

CATALOGO_GLOBAL = pd.DataFrame(
    {
        "Title": ["Stranger Things", "Dark", "The OA", "Fringe", "Primer", "Coherence", "The Matrix", "Inception", "Black Mirror", "Devs"],
        "Genre": ["Ciencia Ficcion", "Ciencia Ficcion", "Ciencia Ficcion", "Ciencia Ficcion", "Ciencia Ficcion", "Ciencia Ficcion", "Accion", "Accion", "Ciencia Ficcion", "Ciencia Ficcion"],
        "Popularity_Score": [98, 85, 60, 50, 15, 20, 95, 99, 90, 30],
    }
)


def encontrar_joyas_ocultas(catalogo: pd.DataFrame, genero_favorito: str, titulos_vistos: list[str], top_n: int = 5) -> pd.DataFrame:
    """Devuelve titulos del genero favorito, no vistos y menos populares."""
    disponibles = catalogo[(catalogo["Genre"] == genero_favorito) & (~catalogo["Title"].isin(titulos_vistos))]
    return disponibles.sort_values("Popularity_Score").head(top_n).reset_index(drop=True)


def graficar_joyas(joyas: pd.DataFrame, ruta_salida: str | Path) -> None:
    """Guarda un grafico de las joyas encontradas."""
    if joyas.empty:
        return
    datos = joyas.sort_values("Popularity_Score")
    plt.figure(figsize=(9, max(3, len(datos) * 0.6)))
    plt.barh(datos["Title"], datos["Popularity_Score"], color="#264653")
    plt.title("Joyas ocultas: menor popularidad, mayor oportunidad")
    plt.xlabel("Puntaje de popularidad")
    plt.tight_layout()
    plt.savefig(ruta_salida)
    plt.close()
