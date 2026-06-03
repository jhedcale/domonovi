import os
import sys
import time

# Forzar inclusión del directorio raíz para que las rutas relativas no rompan nada
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importaciones de toda nuestra arquitectura modular
from src.utils.base_datos import inicializar_tablas, registrar_sospechoso
from src.hardware.energia import MonitorEnergia
from src.hardware.seguridad import GuardianPerimetral
from src.hardware.modem_esim import ControladorModemeSIM
from src.audio.microfono import CapturaAudio
from src.audio.sintetizador import SintetizadorVozLocal
from src.inteligencia.intencionalidad import AnalizadorIntencionalidad
from src.inteligencia.afectiva import FiltroVecinoEbrio

class OrquestadorCasaInteligente:
    def __init__(self):
        print("🧠 Inicializando el Orquestador Central 'IAsafe Local'...")
        # Inicializar el almacenamiento físico
        inicializar_tablas()
        
        # Instanciar todos los controladores modulares
        self.energia = MonitorEnergia()
        self.seguridad = GuardianPerimetral()
        self.esim = ControladorModemeSIM()
        self.microfono = CapturaAudio()
        self.altavoz = SintetizadorVozLocal()
        self.intencionalidad = AnalizadorIntencionalidad()
        self.filtro_ebrio = FiltroVecinoEbrio()

    def ejecutar_ciclo_monitoreo(self):
        print("\n=======================================================")
        print("🔄 [CICLO] Ejecutando escaneo preventivo general de la vivienda...")
        print("=======================================================")
        
        # 1. Monitoreo de subsistema eléctrico y solar
        reporte_luz = self.energia.evaluar_estado_potencia()
        print(f"🔋 Energía: {reporte_luz['voltaje']}V | Estado: {reporte_luz['estado']}")
        
        # 2. Análisis del ruido de la habitación para ajustar nuestra voz
        analisis_ruido = self.microfono.verify_atenuacion_necesaria() if hasattr(self.microfono, 'verify_atenuacion_necesaria') else self.microfono.verificar_atenuacion_necesaria()
        ruido_db = analisis_ruido["ruido_db"]
        
        # 3. Monitoreo de variables químicas (Lazo de Incendio)
        reporte_fuego = self.seguridad.verificar_sensores_incendio()
        if reporte_fuego["peligro"]:
            msg_critico = f"ALERTA CRÍTICA: Se detecta una amenaza de {reporte_fuego['diagnostico']}. Evacúe inmediatamente."
            self.altavoz.emitir_mensaje_voz(msg_critico, ruido_db)
            self.esim.despachar_llamada_emergencia(msg_critico)
            return # Detener ciclo por emergencia extrema
            
        # 4. Monitoreo Perimetral Cognitivo (Simulación de un escenario de merodeo)
        print("\n👀 [Visión Artificial] Analizando presencia humana en acera exterior...")
        eval_intencion = self.intencionalidad.evaluar_comportamiento_perimetral(es_rostro_conocido=False, segundos_en_escena=65)
        
        if eval_intencion["nivel_alerta"] >= 2:
            print(f"⚠ IA detectó anomalía conductual: {eval_intencion['diagnostico']}")
            
            # Aplicamos el filtro del vecino recurrente para ver si de-escalamos
            # Simulamos un mock de base de datos local para verificar el embedding
            mock_db_vector = {"ID_ROSTRO_DESCONOCIDO_001": {"conteo": 7, "habitual": True}}
            datos_familiaridad = self.filtro_ebrio.progresar_frecuencia_desconocido(mock_db_vector, "ID_ROSTRO_DESCONOCIDO_001") if hasattr(self.filtro_ebrio, 'progresar_frecuencia_desconocido') else self.filtro_ebrio.procesar_frecuencia_desconocido(mock_db_vector, "ID_ROSTRO_DESCONOCIDO_001")
            
            dictamen = self.filtro_ebrio.de_escalar_alerta_emocional(eval_intencion["nivel_alerta"], datos_familiaridad)
            
            if dictamen["mensaje_audio"]:
                # Caso de-escalado: El vecino regular actuando de forma no común
                self.altavoz.emitir_mensaje_voz(dictamen["mensaje_audio"], ruido_db)
            else:
                # Caso amenaza real confirmado: Registrar forense y despachar llamada
                print("🚨 AMENAZA CONFIRMADA. Ejecutando protocolos de defensa pasiva...")
                registrar_sospechoso("data/forense/images/captura_urgente.jpg", eval_intencion["diagnostico"], eval_intencion["nivel_alerta"])
                
                msg_policia = f"Alerta residencial automática en Calle Falsa 123. Intruso sospechoso confirmado merodeando con nivel {eval_intencion['nivel_alerta']}."
                self.altavoz.emitir_mensaje_voz("Atención: Sujeto altamente sospechoso detectado afuera. Cerraduras bloqueadas.", ruido_db)
                self.esim.despachar_sms_alerta("+123456789", msg_policia)
        else:
            print("✓ Perímetro seguro. Sin anomalías de movimiento detectadas.")

if __name__ == "__main__":
    orquestador = OrquestadorCasaInteligente()
    # Ejecutamos el gran ciclo integrado de prueba
    orquestador.ejecutar_ciclo_monitoreo()