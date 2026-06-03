import sqlite3
import os
import time
from config.settings import DB_PATH

def conectar_db():
    """Establece conexión con el archivo de base de datos local."""
    return sqlite3.connect(DB_PATH)

def inicializar_tablas():
    """Crea la estructura de la casa inteligente si no existe."""
    conn = conectar_db()
    cursor = conn.cursor()
    
    # 1. Tabla de Usuarios y Roles (Gobernanza)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE,
        rol TEXT CHECK(rol IN ('ADMIN', 'MONIT', 'USER')) NOT NULL
    )""")
    
    # 2. Tabla de Registro de Sospechosos (Fotos y conductas)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registro_sospechosos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp REAL NOT NULL,
        ruta_imagen TEXT NOT NULL,
        conducta_detectada TEXT NOT NULL,
        nivel_alerta INTEGER NOT NULL
    )""")
    
    # 3. Tabla del Algoritmo "Vecino Ebrio" (Frecuencia de desconocidos)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS frecuencia_desconocidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vector_facial_id TEXT UNIQUE NOT NULL,
        conteo_avistamientos INTEGER DEFAULT 1,
        ultima_vez REAL NOT NULL
    )""")
    
    # Crear el usuario del Propietario por defecto como ADMINISTRADOR si está vacío
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO usuarios (nombre, rol) VALUES (?, ?)", ("Propietario Invidente", "ADMIN"))
        
    conn.commit()
    conn.close()
    print("✓ Base de datos local SQLite inicializada con éxito.")

# --- OPERACIONES CRUD CON CONTROL DE ROLES ---

def registrar_usuario(operador_rol, nombre, rol):
    """Solo ADMIN y MONIT pueden crear usuarios."""
    if operador_rol not in ['ADMIN', 'MONIT']:
        return "❌ ERROR: Privilegios insuficientes para registrar usuarios."
    
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nombre, rol) VALUES (?, ?)", (nombre, rol))
        conn.commit()
        return f"✓ Usuario {nombre} registrado como {rol}."
    except sqlite3.IntegrityError:
        return "❌ ERROR: El usuario ya existe."
    finally:
        conn.close()

def listar_usuarios():
    """Cualquiera puede listar los usuarios del sistema."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, rol FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def registrar_sospechoso(ruta_img, conducta, nivel):
    """Guarda automáticamente una foto/registro de sospechoso por intencionalidad."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO registro_sospechosos (timestamp, ruta_imagen, conducta_detectada, nivel_alerta) VALUES (?, ?, ?, ?)",
        (time.time(), ruta_img, conducta, nivel)
    )
    conn.commit()
    conn.close()
    return "✓ Registro forense guardado en la base de datos local."

def eliminar_registro_forense(operador_rol, autenticado_2fa, id_registro):
    """REQUERIMIENTO CRÍTICO: Solo el ADMIN con el DOBLE FACTOR puede borrar."""
    if operador_rol != "ADMIN":
        return "❌ ACCESO DENEGADO: Rol insuficiente. Solo el Administrador puede borrar."
    
    if not autenticado_2fa:
        return "❌ OPERACIÓN BLOQUEADA: Requiere el segundo factor de seguridad activo (SMS/OTP)."
    
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM registro_sospechosos WHERE id = ?", (id_registro,))
    conn.commit()
    conn.close()
    return f"🗑️ Registro forense ID {id_registro} eliminado permanentemente por el Administrador."