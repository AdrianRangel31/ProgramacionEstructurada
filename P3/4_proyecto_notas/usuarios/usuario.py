from conexionBD import *
import datetime

def registrar(nombre,apellidos,email,contrasena):
    try:
        fecha = datetime.datetime.now()
        sql = "insert into usuarios (nombre,apellidos,email,password, fecha) values(%s,%s,%s,%s,%s)"
        val = (nombre,apellidos,email,contrasena,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False
        
def iniciar_sesion(email,contrasena):
    try:
        val=(email,contrasena)
        sql = "select * from usuarios where email = %s and password = %s"
        cursor.execute(sql,val)
        registros = cursor.fetchone()
        if registros:
            return registros
        else: 
            return None
    except:
        return None