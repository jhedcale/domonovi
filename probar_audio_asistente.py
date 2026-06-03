import os
import sys

# Habilitar importaciones de la raíz
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.audio.microfono import CapturaAudio
from src.audio.sintetizador import SintetizadorVozLocal
from src.hardware.seguridad import GuardianPerimetral

print("=== 🧪 PROBANDO CAPA DE AUDIO ASISTENCIAL E INTEGRACIÓN ===")

# Instanciar componentes
microfono = CapturaAudio()
altavoz = SintetizadorVozLocal()
seguridad = GuardianPerimetral()

# 1. Monitorear el entorno auditivo
analisis_cuarto = microfono.verificar_atenuacion_necesaria()
ruido_db = analisis_cuarto["ruido_db"]
print(f"Nivel de ruido medido en la habitación: {ruido_db} dB ({analisis_cuarto['diagnostico']})")

if analisis_cuarto["solicitar_atenuacion_multimedia"]:
    print("🎬 [Hardware] Enviando pulso IR para pausar la televisión y escuchar/hablar...")

# 2. Leer estado de la casa desde el hardware perimetral
print("\n[Hardware] Escaneando ventanas para generar el reporte de voz...")
accesos = seguridad.escanear_puertas_y_ventanas()

# Filtrar cuáles están abiertas para decírselo al usuario de forma humana
abiertas = [acceso.replace('_', ' ').title() for acceso, estado in accesos.items() if estado == "ABIERTA"]

# 3. Construir el diálogo dinámico
if abiertas:
    reporte_texto = f"Atención. He verificado los accesos y las siguientes zonas están abiertas: {', '.join(abiertas)}. Recuerde cerrarlas antes de dormir."
else:
    reporte_texto = "Reporte completado. Todas las puertas y ventanas de la vivienda se encuentran cerradas de forma segura."

# 4. Hablarle al usuario con volumen adaptativo
altavoz.emitir_mensaje_voz(reporte_texto, ruido_db)