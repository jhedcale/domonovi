Param()

# Script para generar `use_cases.svg` y `use_cases.png` desde `use_cases.mmd`.
# Requisitos: Node.js y acceso a `npx` con `@mermaid-js/mermaid-cli`.

Set-Location -Path $PSScriptRoot

Write-Host "Generando diagramas desde $PSScriptRoot/use_cases.mmd..."

# SVG
npx @mermaid-js/mermaid-cli -i use_cases.mmd -o use_cases.svg --width 1000

# PNG (opcional)
npx @mermaid-js/mermaid-cli -i use_cases.mmd -o use_cases.png --width 1400

Write-Host "Generación completada: use_cases.svg y use_cases.png en $PSScriptRoot"
