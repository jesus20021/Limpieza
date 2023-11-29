from datetime import datetime
from modelo_controlador.actividad import Actividad

calendar = datetime(2023, 11, 2)

nueva_actividad = Actividad(1, "Actividad de prueba", "Descripción de la actividad",
                            1, 1, calendar, datetime.now(), None, "pendiente", None)

print("Se creó la actividad correctamente: {}".format(nueva_actividad) if nueva_actividad.crear() else "La actividad no se pudo crear")

print("")

calendar = datetime(2023, 11, 1)
nueva_actividad.estado = "completada"
nueva_actividad.fecha_acabado = calendar
nueva_actividad.foto = "ruta/foto.png"
print("Se actualizó correctamente: {}".format(nueva_actividad) if nueva_actividad.actualizar() else "La actividad no se pudo actualizar")

print("")

lista = Actividad.listar()
print("Lista de actividades: ")
for actividad in lista:
    print("\t{}".format(actividad))

print("")

actividad = Actividad.buscar(1)
if actividad:
    print("Actividad Leída: {}".format(actividad))

    print("")

    print("Se eliminó correctamente: {}".format(actividad) if actividad.eliminar() else "La actividad no se pudo eliminar")
else:
    print("No se pudo leer la actividad")