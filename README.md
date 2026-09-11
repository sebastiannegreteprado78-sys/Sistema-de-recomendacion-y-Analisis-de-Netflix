# Sistema de Recomendación y Análisis de Contenido de Netflix

Proyecto educativo para analizar un historial de visualizacion y generar recomendaciones de contenido.

## Que responde

1. Cuanto tiempo se ha consumido.
2. Que programas y generos predominan.
3. Como cambian las preferencias con el tiempo.
4. Que titulos poco populares pueden ser interesantes.
5. Que contenido es similar segun sus sinopsis.

## Instalacion

Se recomienda Python 3.10 o superior:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows, activa el entorno con `.venv\\Scripts\\activate`.

## Ejecucion

Desde la raiz del proyecto:

```bash
python main.py
```

Los graficos se guardan en `outputs/graficos/`. El notebook de `notebooks/analisis_exploratorio.ipynb` contiene una version paso a paso.

## Estructura

- `data/`: datos de entrada de ejemplo.
- `src/`: funciones reutilizables, separadas por pregunta.
- `main.py`: orquestador del analisis.
- `tests/`: pruebas unitarias.
- `outputs/graficos/`: resultados visuales generados.

Los datos incluidos son ficticios y sirven solo para demostrar el flujo.

## Publicacion segura

El proyecto funciona sin claves API, cuentas externas ni modelos guardados. Para
mantenerlo sencillo y seguro, usa en `data/` solo ejemplos anonimizados. No subas
historiales reales, tokens, contrasenas, archivos `.env`, modelos (`.pkl`,
`.pickle`, `.joblib`, `.onnx`) ni archivos comprimidos. `.gitignore` deja esos
archivos fuera junto con los graficos generados.

Antes de subir cambios, conviene pasar estas comprobaciones:

```bash
git diff --check
git status --short
python -m pip install -r requirements.txt
python -m pytest -q
python -m pip install pip-audit
pip-audit -r requirements.txt
```

Si se cuela una clave o un dato personal, borrarlo después no alcanza. Revoca la
clave, limpia el historial y revisa las copias o forks que puedan existir.

Por ahora es un script local: no ofrece una API ni un panel. Si más adelante se
convierte en un servicio web, habrá que sumar autenticacion y control de acceso.
