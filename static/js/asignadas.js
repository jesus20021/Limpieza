let actividad = (id) => {
    data = {id: id}
    fetch("/getActividad", {
        method:"POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then (response => response.json())
    .then (data => {
        document.getElementById('id').value=data['id'];
        document.getElementById('nombre').textContent=data['nombre'];
        document.getElementById('descripcion').textContent=data['descripcion'];
        fetch("/getColonia", {
                method:"POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({'id':data['colonia']})
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                document.getElementById('colonia').textContent=data['nombre'];
            })
        document.getElementById('fecha').textContent=data['fechaPropuesta'];
    })
    .catch(error => console.log(error))
}
