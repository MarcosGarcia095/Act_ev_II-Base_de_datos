import pymysql

# Conectar a la base de datos MySQL
conexion = pymysql.connect(
    host='localhost',  # Cambia si es necesario
    user='root',       # Usuario de MySQL
    password='',       # Contraseña de MySQL
    database='autos_db' # Nombre de la base de datos
)

try:
    with conexion.cursor() as cursor:
        # Llamada para insertar un auto
        nombre = 'Toyota Corolla'
        anio_fabricacion = 2020
        cursor.callproc('InsertAuto', [nombre, anio_fabricacion])
        conexion.commit()
        print(f"Auto '{nombre}' insertado correctamente.")

        # Consultar los autos
        cursor.callproc('GetAutos')
        for resultado in cursor.fetchall():
            print(f"Auto: {resultado[1]}, Año: {resultado[2]}")

        # Eliminar el auto con ID 1 (asumimos que este es el ID del auto insertado)
        cursor.callproc('DeleteAuto', [1])
        conexion.commit()
        print(f"Auto con ID 1 eliminado correctamente.")

        # Consultar nuevamente para verificar la eliminación
        cursor.callproc('GetAutos')
        autos = cursor.fetchall()
        if autos:
            for auto in autos:
                print(f"Auto: {auto[1]}, Año: {auto[2]}")
        else:
            print("No hay autos en la base de datos.")

finally:
    conexion.close()