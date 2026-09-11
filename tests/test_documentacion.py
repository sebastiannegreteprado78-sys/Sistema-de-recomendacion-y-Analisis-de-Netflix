from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
DOCUMENTOS = (RAIZ / "README.md", RAIZ / "SECURITY.md")
EXPRESIONES_AUTOMATICAS = (
    "cabe destacar",
    "en este sentido",
    "solucion integral",
    "experiencia fluida",
    "de forma sencilla y eficiente",
    "si quieres",
)


def test_documentacion_mantiene_un_tono_directo():
    texto = "\n".join(ruta.read_text(encoding="utf-8").lower() for ruta in DOCUMENTOS)

    encontradas = [frase for frase in EXPRESIONES_AUTOMATICAS if frase in texto]

    assert not encontradas, f"Expresiones que conviene revisar: {encontradas}"