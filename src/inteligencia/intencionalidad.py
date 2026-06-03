import time
import random

class AnalizadorIntencionalidad:
    def __init__(self):
        self.tiempo_merodeo_critico = 60.0  # Segundos máximos antes de activar alerta

    def evaluar_comportamiento_perimetral(self, es_rostro_conocido, segundos_en_escena):
        """
        Analiza de forma analítica el vector de tiempo y el reconocimiento
        para clasificar el nivel de intencionalidad del sujeto en la acera.
        """
        if es_rostro_conocido:
            return {"nivel_alerta": 1, "estado": "NORMAL", "diagnostico": "Familiar o residente detectado."}
            
        # Si el sujeto no es conocido, evaluamos el tiempo de permanencia (Dwell Time)
        if segundos_en_escena < 20:
            return {"nivel_alerta": 1, "estado": "NORMAL", "diagnostico": "Tránsito fluido de desconocido."}
        elif segundos_en_escena < self.tiempo_merodeo_critico:
            return {"nivel_alerta": 2, "estado": "ATENCIÓN", "diagnostico": "Sujeto desconocido merodeando en la entrada."}
        else:
            # Detectamos posturas anómalas simuladas cerca de la cerradura
            postura_sospechosa = random.choice([True, False])
            if postura_sospechosa:
                return {"nivel_alerta": 3, "estado": "SOSPECHA", "diagnostico": "Merodeo extendido con lenguaje corporal de forzado."}
            return {"nivel_alerta": 2, "estado": "ATENCIÓN", "diagnostico": "Merodeo estático prolongado."}