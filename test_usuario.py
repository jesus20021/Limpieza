from modelo_controlador.usuario import Usuario

if __name__ == "__main__":
    nuevo_usuario = Usuario("usuario", "Usuario de prueba", "usuario", "admin", 1)
    print("Se creó el usuario correctamente:", nuevo_usuario) if nuevo_usuario.crear() else print("El usuario no se pudo crear")

    nuevo_usuario.nombre = "Nuevo nombre"
    print("Se actualizó correctamente:", nuevo_usuario) if nuevo_usuario.actualizar() else print("El usuario no se pudo actualizar")

    lista_usuarios = Usuario.listar()
    print("Lista de usuarios: ")
    for usuario in lista_usuarios:
        print("\t", usuario)

    usuario_leido = Usuario.buscar("usuario")
    if usuario_leido:
        print("Usuario Leído:", usuario_leido)
        print("Se eliminó correctamente:", usuario_leido) if usuario_leido.eliminar() else print("El usuario no se pudo eliminar")
    else:
        print("No se pudo leer el usuario")