import os

# Rutas Base del Sistema (Detecta automáticamente dónde está instalado)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "config", "domotica_local.db")
FORENSE_IMG_DIR = os.path.join(BASE_DIR, "data", "forense", "images")

# Clave secreta local para generar los códigos de seguridad del Administrador
SECRET_KEY_2FA = "SUPER_SECRET_COMPUTACION_AFECTIVA_2026"

# Umbrales Críticos de Hardware (Física, Química y Térmica)
UMBRAL_GAS_MQ5 = 200        # Partes por millón (ppm) para detectar fugas
UMBRAL_RUIDO_DB = 75        # Decibelios para pausar música y escuchar al usuario
TEMP_MAX_BANO = 42.0        # Grados Celsius máximo permitido en la ducha
TEMP_MIN_DUCHA = 37.0       # Temperatura ideal de confort