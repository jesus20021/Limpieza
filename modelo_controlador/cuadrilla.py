from modelo_controlador.bd import BD
class Cuadrilla:
    def __init__(self, idCuadrilla, nombre):
        self.idCuadrilla = idCuadrilla
        self.nombre = nombre

    @classmethod
    def buscar(cls, idCuadrilla):
        bd = BD()
        bd.connect()
        consulta = "SELECT * FROM cuadrilla WHERE idCuadrilla = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (idCuadrilla,))
                result = cursor.fetchone()
                if result:
                    cuadrilla = Cuadrilla(result[0], result[1])
                    return cuadrilla
                else:
                    return None
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    @classmethod
    def listar(cls):
        cuadrillas = []
        bd = BD()
        bd.connect()
        consulta = "SELECT * FROM cuadrilla"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta)
                result = cursor.fetchall()
                for row in result:
                    cuadrillas.append(Cuadrilla(row[0], row[1]))
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()
        return cuadrillas

    def actualizar(self):
        bd = BD()
        bd.connect()
        consulta = "UPDATE cuadrilla SET nombre = %s WHERE idCuadrilla = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.nombre, self.idCuadrilla))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def crear(self):
        bd = BD()
        bd.connect()
        consulta = "INSERT INTO cuadrilla(idCuadrilla, nombre) VALUES (%s, %s)"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.idCuadrilla, self.nombre))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def eliminar(self):
        bd = BD()
        bd.connect()
        consulta = "DELETE FROM cuadrilla WHERE idCuadrilla = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.idCuadrilla,))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def __str__(self):
        return self.nombre