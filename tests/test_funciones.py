import pandas as pd
import pytest

from src.evolucion_temporal import calcular_proporciones, construir_tabla_evolucion
from src.joyas_ocultas import CATALOGO_GLOBAL, encontrar_joyas_ocultas
from src.motor_recomendacion import CATALOGO_SINOPSIS, construir_matriz_similitud, recomendar
from src.perfil_preferencias import calcular_top_generos, enriquecer_con_generos
from src.tiempo_consumido import calcular_tiempo_consumido
from src.tiempo_consumido import cargar_actividad


def actividad_prueba():
    return pd.DataFrame(
        {
            "Title": ["The Office: Temporada 1: Capítulo 1", "Dark: Temporada 1: Capítulo 1"],
            "Duration": ["00:22:00", "00:52:00"],
            "Duration_timedelta": pd.to_timedelta(["00:22:00", "00:52:00"]),
            "Date": pd.to_datetime(["2022-01-01", "2023-01-01"]),
        }
    )


def test_calcular_tiempo_consumido():
    assert calcular_tiempo_consumido(actividad_prueba()) == pd.Timedelta("01:14:00")


def test_cargar_actividad_rechaza_duracion_invalida(tmp_path):
    ruta = tmp_path / "actividad.csv"
    pd.DataFrame({"Title": ["Titulo"], "Duration": ["no-es-una-duracion"]}).to_csv(ruta, index=False)

    with pytest.raises(ValueError, match="duracion.*formato invalido"):
        cargar_actividad(ruta)


def test_perfil_y_evolucion():
    enriquecida = enriquecer_con_generos(actividad_prueba())
    assert calcular_top_generos(enriquecida).to_dict() == {"Comedia": 1, "Ciencia Ficcion": 1}
    tabla = construir_tabla_evolucion(enriquecida)
    assert tabla.loc[pd.Period("2022", freq="Y"), "Comedia"] == 1
    assert calcular_proporciones(tabla).loc[pd.Period("2022", freq="Y")].sum() == 100


def test_joyas_y_recomendaciones():
    joyas = encontrar_joyas_ocultas(CATALOGO_GLOBAL, "Ciencia Ficcion", ["Dark"])
    assert "Primer" in joyas["Title"].tolist()
    matriz, _ = construir_matriz_similitud(CATALOGO_SINOPSIS)
    recomendaciones = recomendar("The Office", CATALOGO_SINOPSIS, matriz)
    assert recomendaciones
    assert recomendaciones[0][0] == "Parks and Recreation"
