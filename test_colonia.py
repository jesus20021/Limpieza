from modelo_controlador.colonia import Colonia
nueva_colonia = Colonia(-1, 12345, "Colonia de prueba")
print("Se creó la colonia correctamente:", nueva_colonia) if nueva_colonia.crear() else print("La colonia no se pudo crear")

nueva_colonia.nombre = "Nueva Colonia"
nueva_colonia.codigoPostal = 54321
print("Se actualizó correctamente:", nueva_colonia) if nueva_colonia.actualizar() else print("La colonia no se pudo actualizar")

lista_colonias = Colonia.listar()
print("Lista de colonias: ")
for colonia in lista_colonias:
    print("\t", colonia)

colonia_leida = Colonia.buscar(-1)
if colonia_leida:
    print("Colonia Leída:", colonia_leida)
    print("Se eliminó correctamente:", colonia_leida) if colonia_leida.eliminar() else print("La colonia no se pudo eliminar")
else:
    print("No se pudo leer la colonia")
