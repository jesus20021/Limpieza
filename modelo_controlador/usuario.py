from modelo_controlador.bd import BD

class Usuario:
    def __init__(self, usuario, nombre, contraseña, tipo, cuadrilla):
        self.usuario = usuario
        self.nombre = nombre
        self.contraseña = contraseña
        self.tipo = tipo
        self.cuadrilla = cuadrilla

    @classmethod
    def buscar(cls, usuario):
        bd = BD()
        bd.connect()
        consulta = "SELECT * FROM usuario WHERE usuario = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (usuario,))
                result = cursor.fetchone()
                if result:
                    user = Usuario(result[0], result[1], result[2], result[3], result[4])
                    return user
                else:
                    return None
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    @classmethod
    def listar(cls):
        usuarios = []
        bd = BD()
        bd.connect()
        consulta = "SELECT * FROM usuario"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta)
                result = cursor.fetchall()
                for row in result:
                    usuarios.append(Usuario(row[0], row[1], row[2], row[3], row[4]))
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()
        return usuarios

    @classmethod
    def listarCuadrilla(cls, tipo, cuadrilla):
        usuarios = []
        bd = BD()
        bd.connect()
        consulta = "SELECT * FROM usuario WHERE tipo = %s AND cuadrilla = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (tipo, cuadrilla))
                result = cursor.fetchall()
                for row in result:
                    usuarios.append(Usuario(row[0], row[1], row[2], row[3], row[4]))
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()
        return usuarios

    @classmethod
    def listarTipo(cls, tipo):
        usuarios = []
        bd = BD()
        bd.connect()
        consulta = "SELECT * FROM usuario WHERE tipo = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (tipo,))
                result = cursor.fetchall()
                for row in result:
                    usuarios.append(Usuario(row[0], row[1], row[2], row[3], row[4]))
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()
        return usuarios

    def actualizar(self):
        bd = BD()
        bd.connect()
        consulta = "UPDATE usuario SET nombre = %s, contraseña = %s, tipo = %s, cuadrilla = %s WHERE usuario = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.nombre, self.contraseña, self.tipo, self.cuadrilla, self.usuario))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def crear(self):
        bd = BD()
        bd.connect()
        consulta = "INSERT INTO usuario(usuario, nombre, contraseña, tipo, cuadrilla) VALUES (%s, %s, %s, %s, %s)"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.usuario, self.nombre, self.contraseña, self.tipo, self.cuadrilla))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def eliminar(self):
        bd = BD()
        bd.connect()
        consulta = "DELETE FROM usuario WHERE usuario = %s"
        try:
            with bd.cursor as cursor:
                cursor.execute(consulta, (self.usuario,))
                bd.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(e)
        finally:
            bd.conn.close()

    def __str__(self):
        return self.nombre