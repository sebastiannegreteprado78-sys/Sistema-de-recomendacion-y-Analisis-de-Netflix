# Seguridad

## Alcance actual

El proyecto lee un CSV local y genera graficos. No usa APIs externas, secretos,
autenticacion, modelos serializados ni un servidor web. Los datos de ejemplo son
ficticios; mantenlos asi y no los reemplaces por historiales reales.

## Reglas para contribuir

- No incluy claves, tokens, contrasenas, certificados privados ni archivos `.env`.
- No incluy datos personales o historiales de visualizacion identificables.
- No subas modelos serializados (`pickle`, `joblib` u otros formatos ejecutables)
  sin una revision especifica de su origen y proceso de carga.
- Ejecuta las pruebas y una auditoria de dependencias antes de abrir un pull request.
- Revisa `git diff --check` y `git status --short` antes de hacer push.

## Si se expone un secreto

1. Revoca o rota el secreto inmediatamente.
2. Abre un issue privado o contacta al mantenedor sin pegar el secreto.
3. Elimina el archivo del historial de Git y revisa copias, artefactos y forks.

## Riesgos pendientes si se amplía el proyecto

Si se agrega una API o un panel, habrá que incorporar autenticacion, autorizacion,
validacion de entradas, limites de tamaño, protección de rutas de archivos y logs
sin datos personales. Si se guardan modelos, deben venir de una fuente conocida y
cargarse con un formato que no ejecute código arbitrario.