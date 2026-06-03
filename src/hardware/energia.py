import random
import time

class MonitorEnergia:
    def __init__(self):
        self.voltaje_bateria_nominal = 12.0
        self.voltaje_critico = 10.8  # Umbral donde la batería entra en riesgo de descarga profunda
        self.panel_solar_activo = True

    def leer_voltaje_bateria(self):
        """
        Simula la lectura del convertidor analógico-digital (ADC ADS1115).
        Devuelve el voltaje actual del banco de almacenamiento local de 12V.
        """
        # Simulamos una fluctuación normal entre 10.5V y 13.8V
        voltaje_actual = round(random.uniform(10.5, 13.8), 2)
        return voltaje_actual

    def evaluar_estado_potencia(self):
        """
        Analiza el voltaje actual y determina si el sistema debe entrar en
        modo de ahorro de energía crítico para preservar las funciones de seguridad.
        """
        voltaje = self.leer_voltaje_bateria()
        reporte = {
            "voltaje": voltaje,
            "estado": "NORMAL",
            "accion_requerida": "NINGUNA"
        }

        if voltaje <= self.voltaje_critico:
            reporte["estado"] = "CRÍTICO_BAJO_VOLTAJE"
            reporte["accion_requerida"] = "APAGAR_DOMOTICA_SECUNDARIA_MANTENER_ALARMAS"
        elif voltaje > 13.0:
            reporte["estado"] = "CARGA_COMPLETA_SOLAR"
            
        return reporte

if __name__ == "__main__":
    monitor = MonitorEnergia()
    print("🔋 Probando lecturas de telemetría eléctrica:")
    for _ in range(3):
        print(monitor.evaluar_estado_potencia())
        time.sleep(0.5)
