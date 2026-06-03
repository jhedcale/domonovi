import os
import sys

# Habilitar importaciones de la raíz
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.hardware.energia import MonitorEnergia
from src.hardware.seguridad import GuardianPerimetral

print("=== 🧪 PROBANDO LA CAPA DE HARDWARE Y TELEMETRÍA ===")

# Instanciar controladores
energia = MonitorEnergia()
seguridad = GuardianPerimetral()

print("\n1. Verificando subsistema eléctrico solar:")
reporte_energia = energia.evaluar_estado_potencia()
print(f"Voltaje del Banco de Baterías: {reporte_energia['voltaje']}V")
print(f"Estado de Potencia: {reporte_energia['estado']}")
print(f"Lógica de Mitigación Eléctrica: {reporte_energia['accion_requerida']}")

print("\n2. Escaneando cerramientos perimetrales para el usuario:")
accesos_casa = seguridad.escanear_puertas_y_ventanas()
for acceso, estado in accesos_casa.items():
    print(f" -> El sensor en [{acceso.replace('_', ' ').title()}] reporta: {estado}")

print("\n3. Corriendo test del lazo de seguridad contra incendios:")
reporte_incendio = seguridad.verify_sensores_incendio() if hasattr(seguridad, 'verify_sensores_incendio') else seguridad.verificar_sensores_incendio()
print(f"Diagnóstico Ambiental: {reporte_incendio['diagnostico']}")
if reporte_incendio['peligro']:
    print("🔥 ACCIÓN INMEDIATA: Disparar hilos de interrupción de software prioritarios.")
else:
    print("✓ Sensores químicos y ópticos estables.")

print("\n4. Simulando patrullaje nocturno por regla horaria (Ej: 3:00 AM):")
print(seguridad.monitorear_movimiento_nocturno(3))