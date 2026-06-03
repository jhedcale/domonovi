import time

class SintetizadorVozLocal:
    def __init__(self):
        self.motor_tts = "Piper_Offline_v1"

    def emitir_mensaje_voz(self, texto, ruido_ambiente_db):
        """
        Simula la síntesis de texto a voz (TTS) local, ajustando
        la ganancia (volumen) según los decibelios del entorno.
        """
        # Lógica de volumen adaptativo
        if ruido_ambiente_db >= 75:
            volumen_salida = "100% (Ganancia Máxima por Ruido)"
        elif ruido_ambiente_db >= 55:
            volumen_salida = "75% (Ganancia Moderada)"
        else:
            volumen_salida = "40% (Ganancia Atenuada / Noche)"
            
        print(f"\n🔊 [Altavoz Local - {volumen_salida}]: '{texto}'")
        return "✓ Audio reproducido con éxito."

if __name__ == "__main__":
    tts = SintetizadorVozLocal()
    print("🔊 Probando modulador de voz:")
    tts.emitir_mensaje_voz("Sistema en línea", 45) # Silencioso
    tts.emitir_mensaje_voz("Alerta de Gas detectada", 80) # Ruidoso