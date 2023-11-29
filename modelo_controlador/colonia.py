from modelo_controlador.bd import BD

class Colonia:
    def __init__(self, id, codigoPostal, nombre):
        self.id = id
        self.codigoPostal = codigoPostal
        self.nombre = nombre

    @classmethod
    def buscar(cls, id):
        bd = BD()
        bd.connect()
        consulta = "SELECT * FROM colonia WHERE id = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (id,))
                result = cursor.fetchone()
                if result:
                    colonia = Colonia(result[0], result[1], result[2])
                    return colonia
                else:
                    return None
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    @classmethod
    def listar(cls):
        colonias = []
        bd = BD()
        bd.connect()
        consulta = "SELECT * FROM colonia"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta)
                result = cursor.fetchall()
                for row in result:
                    colonias.append(Colonia(row[0], row[1], row[2]))
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()
        return colonias

    def actualizar(self):
        bd = BD()
        bd.connect()
        consulta = "UPDATE colonia SET codigoPostal = %s, nombre = %s WHERE id = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.codigoPostal, self.nombre, self.id))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def crear(self):
        bd = BD()
        bd.connect()
        consulta = "INSERT INTO colonia(id, codigoPostal, nombre) VALUES (%s, %s, %s)"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.id, self.codigoPostal, self.nombre))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def eliminar(self):
        bd = BD()
        bd.connect()
        consulta = "DELETE FROM colonia WHERE id = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.id,))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def __str__(self):
        return f"{self.nombre}, {self.codigoPostal}"