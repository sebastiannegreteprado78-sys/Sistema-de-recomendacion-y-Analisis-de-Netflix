"""Pregunta 3: evolucion temporal de los gustos."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def construir_tabla_evolucion(actividad: pd.DataFrame, periodo: str = "Y") -> pd.DataFrame:
    """Cuenta reproducciones por genero y periodo (Y, Q o M)."""
    if "Date" not in actividad.columns:
        raise ValueError("La actividad necesita una columna Date para analizar la evolucion")
    datos = actividad.dropna(subset=["Date", "Genre"]).copy()
    datos["Periodo"] = pd.to_datetime(datos["Date"]).dt.to_period(periodo)
    return pd.crosstab(datos["Periodo"], datos["Genre"])


def calcular_proporciones(conteos: pd.DataFrame) -> pd.DataFrame:
    """Convierte conteos por periodo en porcentajes por fila."""
    totales = conteos.sum(axis=1).replace(0, pd.NA)
    return conteos.div(totales, axis=0).fillna(0) * 100


def graficar_evolucion(conteos: pd.DataFrame, proporciones: pd.DataFrame, ruta_salida: str | Path) -> None:
    """Guarda la evolucion absoluta y relativa en una figura de dos paneles."""
    fig, ejes = plt.subplots(2, 1, figsize=(12, 9), sharex=True)
    conteos.plot(ax=ejes[0], marker="o")
    ejes[0].set_title("Evolucion del consumo por genero")
    ejes[0].set_ylabel("Reproducciones")
    ejes[0].legend(title="Genero", loc="upper left")
    proporciones.plot.area(ax=ejes[1], stacked=True, alpha=0.85)
    ejes[1].set_title("Proporcion relativa")
    ejes[1].set_ylabel("Porcentaje")
    ejes[1].set_xlabel("Periodo")
    ejes[1].legend(title="Genero", loc="upper left")
    fig.tight_layout()
    fig.savefig(ruta_salida)
    plt.close(fig)
