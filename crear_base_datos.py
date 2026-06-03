import os
import sys

# Permitir que Python encuentre los módulos dentro de la carpeta src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.utils.base_datos import inicializar_tablas, registrar_usuario, listar_usuarios, registrar_sospechoso, eliminar_registro_forense
from src.utils.autenticador import generar_otp_local, validar_otp_local

print("=== 🧪 PROBANDO EL MOTOR DE DATOS LOCAL ===")
# Inicializar la base de datos física (.db)
inicializar_tablas()

print("\n1. Probando creación de usuarios según sus privilegios:")
print(registrar_usuario("USER", "Intruso", "ADMIN"))       # Debe fallar (Un usuario común no puede crear a nadie)
print(registrar_usuario("ADMIN", "Carlos Vidente", "MONIT")) # Debe funcionar (ADMIN crea un Monitor)

print("\n2. Lista actual de usuarios en la casa:")
print(listar_usuarios())

print("\n3. Registrando un sospechoso en el perímetro:")
print(registrar_sospechoso("data/forense/images/sospechoso1.jpg", "Merodeo en ventana", 3))

print("\n4. Probando la seguridad extrema de borrado (Doble Factor):")
# Intento 1: Un usuario común intenta borrar
print(eliminar_registro_forense("USER", False, 1))

# Intento 2: El administrador intenta borrar pero sin poner el código SMS
print(eliminar_registro_forense("ADMIN", False, 1))

# Intento 3: Flujo de éxito del Administrador
print("\n[Simulación]: El Administrador pasa la voz y se genera el código SMS...")
codigo_sms = generar_otp_local("Propietario Invidente")
print(f"[eSIM]: SMS enviado al celular del Administrador. Código recibido: {codigo_sms}")

# El administrador ingresa el código antes de 60 segundos
codigo_correcto = validar_otp_local("Propietario Invidente", codigo_sms)
print(f"¿Código validado con éxito?: {codigo_correcto}")

# El sistema libera el borrado
print(eliminar_registro_forense("ADMIN", codigo_correcto, 1))