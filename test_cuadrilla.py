from modelo_controlador.cuadrilla import Cuadrilla

nueva_cuadrilla = Cuadrilla(-1, "Cuadrilla de prueba")
print("Se creó la cuadrilla correctamente:", nueva_cuadrilla) if nueva_cuadrilla.crear() else print("La cuadrilla no se pudo crear")

nueva_cuadrilla.nombre = "Nuevo nombre"
print("Se actualizó correctamente:", nueva_cuadrilla) if nueva_cuadrilla.actualizar() else print("La cuadrilla no se pudo actualizar")

lista_cuadrillas = Cuadrilla.listar()
print("Lista de cuadrillas: ")
for cuadrilla in lista_cuadrillas:
    print("\t", cuadrilla)

cuadrilla_leida = Cuadrilla.buscar(-1)
if cuadrilla_leida:
    print("Cuadrilla Leída:", cuadrilla_leida)
    print("Se eliminó correctamente:", cuadrilla_leida) if cuadrilla_leida.eliminar() else print("La cuadrilla no se pudo eliminar")
else:
    print("No se pudo leer la cuadrilla")