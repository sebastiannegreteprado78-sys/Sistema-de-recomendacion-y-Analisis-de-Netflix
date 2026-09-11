"""Pregunta 1: tiempo total de visualizacion."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def cargar_actividad(ruta: str | Path) -> pd.DataFrame:
    """Carga la actividad y normaliza sus columnas de fecha y duracion."""
    actividad = pd.read_csv(ruta)
    columnas_requeridas = {"Title", "Duration"}
    faltantes = columnas_requeridas - set(actividad.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {sorted(faltantes)}")
    actividad["Duration_timedelta"] = pd.to_timedelta(actividad["Duration"], errors="coerce")
    duraciones_invalidas = actividad["Duration"].notna() & actividad["Duration_timedelta"].isna()
    if duraciones_invalidas.any():
        cantidad = int(duraciones_invalidas.sum())
        raise ValueError(f"Hay {cantidad} duracion(es) con un formato invalido")
    if "Date" in actividad.columns:
        actividad["Date"] = pd.to_datetime(actividad["Date"], errors="coerce")
    return actividad


def calcular_tiempo_consumido(actividad: pd.DataFrame) -> pd.Timedelta:
    """Suma las duraciones validas de la actividad."""
    duraciones = actividad.get("Duration_timedelta")
    if duraciones is None:
        duraciones = pd.to_timedelta(actividad["Duration"], errors="coerce")
    return duraciones.sum()


def formatear_tiempo(tiempo: pd.Timedelta) -> str:
    """Devuelve una duracion legible en dias, horas y minutos."""
    componentes = tiempo.components
    return f"{componentes.days} dias, {componentes.hours} horas y {componentes.minutes} minutos"


def graficar_duraciones(actividad: pd.DataFrame, ruta_salida: str | Path) -> None:
    """Guarda un grafico con la duracion de cada titulo."""
    datos = actividad.copy()
    datos["Duracion_minutos"] = datos["Duration_timedelta"].dt.total_seconds() / 60
    datos = datos.dropna(subset=["Duracion_minutos"]).sort_values("Duracion_minutos")
    if datos.empty:
        return
    plt.figure(figsize=(10, max(4, len(datos) * 0.45)))
    sns.barplot(data=datos, x="Duracion_minutos", y="Title", hue="Title", legend=False, palette="viridis")
    plt.title("Tiempo de visualizacion por titulo")
    plt.xlabel("Duracion (minutos)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(ruta_salida)
    plt.close()
