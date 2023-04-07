import sqlite3

def conectar_sqlite():
    conexion=sqlite3.connect("clases\\BDSalon.db")
    cursor=conexion.cursor()
    return conexion,cursor

def conexionBD():
    conexion,cursor=conectar_sqlite()

    try:
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS datos(
                            ID INTEGER PRIMARY KEY,
                            Nombre VARCHAR(50) NOT NULL,
                            Fecha datetime NOT NULL,
                            Telefono int(10),
                            Asistencia VARCHAR(10)
                        )
                    ''')
        
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS inventario(
                            ID INTEGER PRIMARY KEY,
                            Nombre VARCHAR(50) NOT NULL,
                            Proovedor VARCHAR(50) NOT NULL,
                            Color VARCHAR(20),
                            Cantidad int(10),
                            Vendido int(10)
                        )
                    ''')
        
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS ventas(
                            ID INTEGER PRIMARY KEY,
                            Fecha datetime NOT NULL,
                            Nombre VARCHAR(50) NOT NULL,
                            Proovedor VARCHAR(50) NOT NULL,
                            Vendido int(10),
                            Total int(10)
                        )
                    ''')
        print("CONEXION EXITOSA")
    except:
        print("CONEXION ERROR")
    conexion.close()

def insertar(datos):
    conexion,cursor=conectar_sqlite()
    sql="""
        INSERT INTO datos (Nombre,Fecha,Telefono,Asistencia)
        VALUES (?,?,?,?)
    """
    if(cursor.execute(sql,datos)):
        conexion.commit()#commit es para actualizar los datos
        conexion.close()
        return True
    else:
        print("No se pudo guardar los datos")
        return False

def actualizar_cita(campo1,dato,campo2):
    conexion,cursor=conectar_sqlite()
    sql="INSERT datos SET "+dato+"where "+campo1+"="+campo2
    if(cursor.execute(sql,dato)):
        print("datos guardados")
        conexion.commit()#commit es para actualizar los datos
        conexion.close()
        return True
    else:
        print("No se pudo guardar los datos")
        return False

def mostrar_citas():
    conexion,cursor=conectar_sqlite()
    
    try:
        datos=cursor.execute("""SELECT * FROM datos
                            order by fecha DESC""")
    except:
        pass
    return datos

def mostrar_inventario():
    conexion,cursor=conectar_sqlite()
    
    try:
        datos=cursor.execute("""SELECT * FROM inventario""")
    except:
        pass
    return datos

def mostrar_ventas():
    conexion,cursor=conectar_sqlite()
    
    try:
        datos=cursor.execute("""SELECT * FROM ventas order by fecha DESC""")
    except:
        pass
    return datos

if __name__ == "__main__":
    conexionBD()