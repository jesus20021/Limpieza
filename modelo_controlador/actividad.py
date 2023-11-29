from modelo_controlador.bd import BD
from datetime import datetime

class Actividad:
    def __init__(self, id, nombre, descripcion, colonia, cuadrilla, fechaPropuesta, fechaCreacion, fechaAcabado, estado, foto):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.colonia = colonia
        self.cuadrilla = cuadrilla
        self.fechaPropuesta = fechaPropuesta
        self.fechaCreacion = fechaCreacion
        self.fechaAcabado = fechaAcabado
        self.estado = estado
        self.foto = foto

    @classmethod
    def buscar(cls, id):
        bd = BD()
        bd.connect()
        consulta = "SELECT * FROM actividad WHERE id = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (id,))
                result = cursor.fetchone()
                if result:
                    actividad = Actividad(result[0], result[1], result[2], result[3], result[4],
                                          result[5], result[6], result[7], result[8], result[9])
                    return actividad
                else:
                    return None
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    @classmethod
    def listar(cls):
        bd = BD()
        bd.connect()
        actividades = []
        consulta = "SELECT * FROM actividad"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta)
                result = cursor.fetchall()
                for row in result:
                    actividad = Actividad(row[0], row[1], row[2], row[3], row[4],
                                          row[5], row[6], row[7], row[8], row[9])
                    actividades.append(actividad)
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()
        return actividades

    @classmethod
    def listarColonia(cls, colonia):
        bd = BD()
        bd.connect()
        actividades = []
        consulta = "SELECT * FROM actividad WHERE colonia = %s AND estado = 'completada'"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (colonia,))
                result = cursor.fetchall()
                for row in result:
                    actividad = Actividad(row[0], row[1], row[2], row[3], row[4],
                                          row[5], row[6], row[7], row[8], row[9])
                    actividades.append(actividad)
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()
        return actividades

    @classmethod
    def listarCuadrillaPendiente(cls, cuadrilla):
        bd = BD()
        bd.connect()
        actividades = []
        consulta = "SELECT * FROM actividad WHERE cuadrilla = %s AND estado = 'pendiente'"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (cuadrilla,))
                result = cursor.fetchall()
                for row in result:
                    actividad = Actividad(row[0], row[1], row[2], row[3], row[4],
                                          row[5], row[6], row[7], row[8], row[9])
                    actividades.append(actividad)
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()
        return actividades
    
    @classmethod
    def listarCuadrilla(cls, cuadrilla):
        bd = BD()
        bd.connect()
        actividades = []
        consulta = "SELECT * FROM actividad WHERE cuadrilla = %s AND estado = 'completada'"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (cuadrilla,))
                result = cursor.fetchall()
                for row in result:
                    actividad = Actividad(row[0], row[1], row[2], row[3], row[4],
                                          row[5], row[6], row[7], row[8], row[9])
                    actividades.append(actividad)
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()
        return actividades

    def actualizar(self):
        bd = BD()
        bd.connect()
        consulta = "UPDATE actividad SET nombre = %s, descripcion = %s, colonia = %s, cuadrilla = %s, " \
                   "fechaPropuesta = %s, fechaCreacion = %s, fechaAcabado = %s, estado = %s, foto = %s WHERE id = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.nombre, self.descripcion, self.colonia, self.cuadrilla,
                                          self.fechaPropuesta, self.fechaCreacion, self.fechaAcabado,
                                          self.estado, self.foto, self.id))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def crear(self):
        bd = BD()
        bd.connect()
        consulta = "INSERT INTO actividad(id, nombre, descripcion, colonia, cuadrilla, fechaPropuesta, " \
                   "fechaCreacion, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, 'pendiente')"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.id, self.nombre, self.descripcion, self.colonia, self.cuadrilla,
                                          self.fechaPropuesta, datetime.now()))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def eliminar(self):
        bd = BD()
        bd.connect()
        consulta = "DELETE FROM actividad WHERE id = %s"
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
        return self.nombre