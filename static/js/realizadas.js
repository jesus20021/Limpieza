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
        document.getElementById('fecha').textContent=data['fechaAcabado'];
        document.getElementById('img').src = "/static/img/"+data['foto']
    })
    .catch(error => console.log(error))
}