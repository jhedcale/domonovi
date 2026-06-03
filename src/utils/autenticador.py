import random
import time

# Memoria temporal RAM para guardar los códigos válidos por 60 segundos sin usar internet
_otp_pool_local = {}

def generar_otp_local(nombre_usuario):
    """Genera un código de 4 dígitos válido por 60 segundos."""
    codigo = str(random.randint(1000, 9999))
    _otp_pool_local[nombre_usuario] = {
        "codigo": codigo,
        "expira": time.time() + 60.0
    }
    return codigo

def validar_otp_local(nombre_usuario, codigo_ingresado):
    """Verifica si el código es correcto y no ha expirado."""
    if nombre_usuario not in _otp_pool_local:
        return False
    
    datos_token = _otp_pool_local[nombre_usuario]
    
    if time.time() > datos_token["expira"]:
        if nombre_usuario in _otp_pool_local:
            del _otp_pool_local[nombre_usuario]
        print("⚠ El código de seguridad ha expirado.")
        return False
    
    if datos_token["codigo"] == str(codigo_ingresado):
        del _otp_pool_local[nombre_usuario] # Se destruye para que no se use dos veces
        return True
        
    return False