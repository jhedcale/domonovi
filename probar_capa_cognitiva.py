import os
import sys

# Habilitar importaciones
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.inteligencia.intencionalidad import AnalizadorIntencionalidad
from src.inteligencia.afectiva import FiltroVecinoEbrio
from src.audio.sintetizador import SintetizadorVozLocal

print("=== 🧪 PROBANDO CAPA COGNITIVA E INTELIGENCIA CONDUCTUAL ===")

# Instanciar el cerebro del sistema
analizador = AnalizadorIntencionalidad()
filtro_ebrio = FiltroVecinoEbrio()
altavoz = SintetizadorVozLocal()

# Simulador de memoria RAM que imita temporalmente a SQLite para la prueba
base_datos_frecuencia_mock = {
    "VECTOR_FACIAL_XYZ_789": {"conteo": 6, "habitual": True} # Este es el vecino recurrente
}

print("\n🚨 ESCENARIO: Sujeto desconocido pasa 75 segundos estático en el porche a las 2:00 AM.")
# 1. El analizador de intencionalidad procesa el tiempo y el rostro desconocido
evaluacion_inicial = analizador.evaluar_comportamiento_perimetral(es_rostro_conocido=False, segundos_en_escena=75)
print(f" -> Diagnóstico Inicial de IA: {evaluacion_inicial['diagnostico']}")
print(f" -> Alerta Propuesta: Nivel {evaluacion_inicial['nivel_alerta']} ({evaluacion_inicial['estado']})")

# 2. El sistema extrae el ID matemático del rostro y consulta su frecuencia histórica
print("\n🔍 [Cerebro] Analizando huella facial contra historial de familiaridad perimetral...")
datos_vecino = filtro_ebrio.procesar_frecuencia_desconocido(base_datos_frecuencia_mock, "VECTOR_FACIAL_XYZ_789")
print(f" -> Frecuencia de este desconocido: {datos_vecino['conteo']} avistamientos previos.")
print(f" -> ¿Es catalogado como habitual seguro?: {datos_vecino['habitual']}")

# 3. Aplicamos el algoritmo del Vecino Ebrio (De-escalado analítico)
dictamen_final = filtro_ebrio.de_escalar_alerta_emocional(evaluacion_inicial['nivel_alerta'], datos_vecino)
print(f"\n⚡ [Dictamen Final Aplicando Computación Afectiva]:")
print(f" -> Nivel de Alerta Ajustado por la IA: Nivel {dictamen_final['nivel_alerta_final']}")

# 4. El sistema le reporta al usuario invidente con el tono calmado correspondiente
if dictamen_final['mensaje_audio']:
    texto_a_hablar = dictamen_final['mensaje_audio']
else:
    texto_a_hablar = "Alerta de seguridad activa. Sujeto sospechoso no identificado en el perímetro."

altavoz.emitir_mensaje_voz(texto_a_hablar, ruido_ambiente_db=40)