import random
import time

class GuardianPerimetral:
    def __init__(self):
        # Mapeo físico de los accesos de la vivienda
        self.accesos = {
            "puerta_principal": "CERRADA",
            "puerta_patio": "CERRADA",
            "ventana_sala": "CERRADA",
            "ventana_cocina": "CERRADA",
            "ventana_bano": "CERRADA"
        }
        
    def escanear_puertas_y_ventanas(self):
        """
        Simula la lectura física de los sensores magnéticos (Reed Switches MC-38).
        Devuelve el estado real actual de cada acceso de la casa.
        """
        # Simulamos aleatoriamente que un acceso podría quedarse abierto por descuido
        for acceso in self.accesos:
            self.accesos[acceso] = random.choice(["CERRADA", "CERRADA", "ABIERTA"])
        return self.accesos

    def verificar_sensores_incendio(self):
        """
        Monitorea el lazo analógico del sensor de humo MQ-2 y el sensor óptico de llama.
        Si detecta anomalías químicas o térmicas, genera una bandera de peligro inmediato.
        """
        lectura_humo_ppm = random.randint(50, 400) # Simulación de ambiente
        presencia_flama = random.choice([False, False, False, False, True]) # 20% probabilidad de fuego en prueba
        
        peligro_detectado = False
        motivo = "AMBIENTE_SEGURO"
        
        # Si supera el umbral de 200 ppm configurado en settings o hay flama directa
        if lectura_humo_ppm >= 200 or presencia_flama:
            peligro_detectado = True
            motivo = f"INCENDIO_DETECTADO (Humo: {lectura_humo_ppm}ppm, Flama: {presencia_flama})"
            
        return {
            "peligro": peligro_detectado,
            "lectura_humo": lectura_humo_ppm,
            "presencia_flama": presencia_flama,
            "diagnostico": motivo
        }

    def monitorear_movimiento_nocturno(self, hora_actual_militar):
        """
        Activa la red de sensores PIR y microondas en la franja nocturna.
        Detecta movimientos inusuales que alimentarán al protocolo de intencionalidad.
        """
        # El modo nocturno opera estrictamente entre las 22:00 y las 06:00
        if hora_actual_militar >= 22 or hora_actual_militar <= 6:
            movimiento_detectado = random.choice([False, True])
            if movimiento_detectado:
                return "🚨 ALERTA: Movimiento perimetral nocturno detectado en zona de tránsito."
        return "✓ Perímetro en calma."

if __name__ == "__main__":
    guardian = GuardianPerimetral()
    print("🚪 Probando escáner de accesos e incendios:")
    print("Estado de Accesos:", guardian.escanear_puertas_y_ventanas())
    print("Monitoreo de Incendios:", guardian.verificar_sensores_incendio())