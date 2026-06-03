import random
import time
from config.settings import UMBRAL_RUIDO_DB

class CapturaAudio:
    def __init__(self):
        self.umbral_ruido = UMBRAL_RUIDO_DB

    def medir_ruido_ambiente(self):
        """
        Simula la lectura del nivel de ruido en decibelios (dB) 
        capturado por el hardware de procesamiento de señal.
        """
        # Fluctuación normal entre un cuarto silencioso (40dB) y la televisión alta (85dB)
        return random.randint(40, 85)

    def verificar_atenuacion_necesaria(self):
        """
        Si el ruido del entorno supera el umbral configurado, ordena congelar
        o bajar el volumen de los equipos multimedia para escuchar al usuario.
        """
        ruido_actual = self.medir_ruido_ambiente()
        atenuar = ruido_actual >= self.umbral_ruido
        
        return {
            "ruido_db": ruido_actual,
            "solicitar_atenuacion_multimedia": atenuar,
            "diagnostico": "ENTORNO_RUIDOSO_ACTIVANDO_FILTROS" if atenuar else "ENTORNO_OPTIMO"
        }

if __name__ == "__main__":
    audio = CapturaAudio()
    print("🎙️ Probando análisis de ruido ambiental:")
    for _ in range(3):
        print(audio.verificar_atenuacion_necesaria())
        time.sleep(0.5)