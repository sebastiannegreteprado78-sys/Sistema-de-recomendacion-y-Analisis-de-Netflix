"""Ejecuta las cinco preguntas del proyecto en orden."""

from pathlib import Path

from src.estilo import aplicar_estilo_minimalista, preparar_directorio_salida
from src.evolucion_temporal import calcular_proporciones, construir_tabla_evolucion, graficar_evolucion
from src.joyas_ocultas import CATALOGO_GLOBAL, encontrar_joyas_ocultas, graficar_joyas
from src.motor_recomendacion import CATALOGO_SINOPSIS, construir_matriz_similitud, recomendar
from src.perfil_preferencias import calcular_top_generos, enriquecer_con_generos, graficar_preferencias
from src.tiempo_consumido import calcular_tiempo_consumido, cargar_actividad, formatear_tiempo, graficar_duraciones


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "sample_viewing_activity.csv"
OUTPUT_PATH = ROOT / "outputs" / "graficos"


def main() -> None:
    aplicar_estilo_minimalista()
    preparar_directorio_salida(OUTPUT_PATH)

    actividad = cargar_actividad(DATA_PATH)
    tiempo_total = calcular_tiempo_consumido(actividad)
    print("1. Tiempo consumido")
    print(f"   {formatear_tiempo(tiempo_total)}")
    graficar_duraciones(actividad, OUTPUT_PATH / "01_tiempo_consumido.png")

    perfil = enriquecer_con_generos(actividad)
    top_generos = calcular_top_generos(perfil)
    print("\n2. Perfil de preferencias")
    print(f"   Genero principal: {top_generos.index[0] if not top_generos.empty else 'sin datos'}")
    print(top_generos.to_string().replace("\n", "\n   "))
    graficar_preferencias(perfil, OUTPUT_PATH / "02_perfil_preferencias.png")

    conteos = construir_tabla_evolucion(perfil)
    proporciones = calcular_proporciones(conteos)
    print("\n3. Evolucion temporal")
    print(conteos.to_string())
    graficar_evolucion(conteos, proporciones, OUTPUT_PATH / "03_evolucion_temporal.png")

    titulos_vistos = perfil["Programa"].dropna().unique().tolist()
    genero_favorito = top_generos.index[0] if not top_generos.empty else "Ciencia Ficcion"
    joyas = encontrar_joyas_ocultas(CATALOGO_GLOBAL, genero_favorito, titulos_vistos)
    print(f"\n4. Joyas ocultas de {genero_favorito}")
    print(joyas[["Title", "Popularity_Score"]].to_string(index=False) if not joyas.empty else "   Sin resultados")
    graficar_joyas(joyas, OUTPUT_PATH / "04_joyas_ocultas.png")

    matriz, _ = construir_matriz_similitud(CATALOGO_SINOPSIS)
    print("\n5. Recomendaciones")
    for titulo in ("The Office", "Stranger Things"):
        recomendaciones = recomendar(titulo, CATALOGO_SINOPSIS, matriz)
        print(f"   Si te gusto {titulo}: {recomendaciones}")


if __name__ == "__main__":
    main()
