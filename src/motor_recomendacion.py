"""Pregunta 5: recomendaciones basadas en similitud textual."""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CATALOGO_SINOPSIS = pd.DataFrame(
    {
        "Title": ["The Office", "Parks and Recreation", "Stranger Things", "Dark", "Space Force"],
        "Sinopsis": [
            "Documental falso sobre el dia a dia en una oficina de ventas de papel. Comedia de trabajo.",
            "Documental falso sobre el dia a dia en el departamento de parques de una ciudad. Comedia de trabajo.",
            "Un nino desaparece en un pueblo con secretos, experimentos del gobierno y monstruos de otra dimension.",
            "La desaparicion de un nino en un pueblo aleman desata viajes en el tiempo y secretos familiares.",
            "Comedia de trabajo sobre un grupo intentando crear la nueva fuerza espacial militar.",
        ],
    }
)

STOPWORDS_ES = ["de", "la", "que", "el", "en", "y", "a", "los", "del", "se", "las", "un", "una", "por", "con", "no", "su", "para", "es", "al", "lo", "como", "mas", "o", "sobre", "sus", "entre"]


def construir_matriz_similitud(catalogo: pd.DataFrame) -> tuple:
    """Vectoriza sinopsis y calcula similitud coseno entre titulos."""
    vectorizador = TfidfVectorizer(stop_words=STOPWORDS_ES)
    matriz_tfidf = vectorizador.fit_transform(catalogo["Sinopsis"])
    return cosine_similarity(matriz_tfidf, matriz_tfidf), vectorizador


def recomendar(titulo: str, catalogo: pd.DataFrame, matriz_similitud, top_n: int = 2) -> list[tuple[str, float]]:
    """Devuelve los titulos mas similares al titulo indicado."""
    indices = pd.Series(catalogo.index, index=catalogo["Title"]).drop_duplicates()
    if titulo not in indices:
        return []
    indice = indices[titulo]
    candidatos = [
        (i, score)
        for i, score in enumerate(matriz_similitud[indice])
        if i != indice and score > 0
    ]
    candidatos.sort(key=lambda item: item[1], reverse=True)
    return [(catalogo.iloc[i]["Title"], float(score)) for i, score in candidatos[:top_n]]
