# Generación del diagrama de Casos de Uso

Archivos:
- `use_cases.mmd` — definición Mermaid del diagrama.
- `use_cases.md` — versión en Markdown con el bloque Mermaid y leyenda.
- `generate_diagram.ps1` — script PowerShell para generar `use_cases.svg` y `use_cases.png`.

Requisitos:
- Node.js
- `npx` (incluido con Node.js)

Comandos (PowerShell):

```powershell
cd "docs"
# Ejecuta el script (usa npx para descargar/ejecutar mermaid-cli localmente)
.\n+\generate_diagram.ps1
```

Si no quieres usar el script, puedes ejecutar directamente:

```powershell
npx @mermaid-js/mermaid-cli -i docs/use_cases.mmd -o docs/use_cases.svg --width 1000
npx @mermaid-js/mermaid-cli -i docs/use_cases.mmd -o docs/use_cases.png --width 1400
```
