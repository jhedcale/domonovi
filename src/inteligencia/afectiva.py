import time

class FiltroVecinoEbrio:
    def __init__(self):
        pass

    def procesar_frecuencia_desconocido(self, db_cursor, vector_id):
        """
        Simula la consulta en la tabla `frecuencia_desconocidos` para ver
        cuántas veces ha pasado este mismo rostro no identificado por la casa.
        """
        # Simulamos la consulta SQL local
        # En producción esto lee los registros de nuestra base de datos SQLite
        timestamp_actual = time.time()
        
        # Simulamos que el sistema recupera el historial de este ID matemático
        # Devuelve: (id, conteo_avistamientos, es_habitual_seguro)
        registro_simulado = db_cursor.get(vector_id, {"conteo": 1, "habitual": False})
        
        # Incrementamos el conteo de avistamientos por este evento actual
        registro_simulado["conteo"] += 1
        
        # Si ha pasado más de 5 veces este mes, la IA lo cataloga como "Regular de la zona"
        if registro_simulado["conteo"] >= 5:
            registro_simulado["habitual"] = True
            
        db_cursor[vector_id] = registro_simulado
        return registro_simulado

    def de_escalar_alerta_emocional(self, nivel_alerta_original, datos_frecuencia):
        """
        Aplica la Computación Afectiva: Modifica la severidad de la alerta
        si se comprueba que el comportamiento anómalo viene de un vecino habitual.
        """
        if nivel_alerta_original >= 2 and datos_frecuencia["habitual"]:
            return {
                "nivel_alerta_final": 2, # No permite que escale a alarma crítica (Nivel 3 o 4)
                "notificacion_usuario": "Sutil",
                "mensaje_audio": "Persona habitual del vecindario transita afuera. No se detecta peligro."
            }
        return {
            "nivel_alerta_final": nivel_alerta_original,
            "notificacion_usuario": "Estándar/Crítica",
            "mensaje_audio": None
        }
