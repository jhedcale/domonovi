# Diagrama de Casos de Uso — IAsafe Local

A continuación está el diagrama de casos de uso en formato Mermaid y una leyenda. Para generar imágenes (SVG/PNG) usa el script provisto en `docs/generate_diagram.ps1`.

```mermaid
%% Diagrama de casos de uso para el proyecto IAsafe Local
usecaseDiagram
actor Usuario
actor Administrador
actor "Dispositivo IoT" as IoT
actor "Servicio Emergencias" as Emergencias
actor "Modelos IA / Cloud" as IA

Usuario --> (Interactuar con asistente)
Usuario --> (Configurar sistema)
Administrador --> (Gestionar base de datos)
IoT --> (Reportar sensores)
IoT --> (Enviar telemetría)

(Interactuar con asistente) ..> (Capturar audio) : includes
(Interactuar con asistente) ..> (Analizar intención) : includes
(Interactuar con asistente) ..> (Emitir voz) : includes

(Monitoreo continuo) --> (Monitorear energía)
(Monitoreo continuo) --> (Verificar incendios)
(Monitoreo continuo) --> (Monitoreo perimetral)

(Monitoreo perimetral) ..> (Analizar intención) : includes
(Monitoreo perimetral) ..> (Analizar afecto/emoción) : includes
(Analizar intención) ..> (Registrar sospechoso) : extends

(Verificar incendios) ..> (Despachar emergencia) : includes
(Registrar sospechoso) ..> (Despachar emergencia) : includes
(Despachar emergencia) --> Emergencias

(Analizar intención) --> IA
(Analizar afecto/emoción) --> IA
```

**Leyenda breve**
- **Actores:** Usuario, Administrador, Dispositivo IoT, Servicio Emergencias, Modelos IA / Cloud.
- **Casos clave:** Interactuar con asistente (captura → análisis → síntesis), Monitoreo continuo (energía, incendios, perímetro), Registrar sospechoso (forense), Despachar emergencia (llamada/SMS), Gestionar base de datos.
- **Ubicación del orquestador:** flujo principal en [src/main.py](src/main.py).

---

Archivos asociados:
- `docs/use_cases.mmd` — definición pura Mermaid para generar imágenes.
- `docs/generate_diagram.ps1` — script PowerShell para generar `use_cases.svg` y `use_cases.png` (usa `npx @mermaid-js/mermaid-cli`).
