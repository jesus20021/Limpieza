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
        console.log(data)
        document.getElementById('id').value = data['id'];
        document.getElementById('nombre').value = data['nombre'];
        document.getElementById('descripcion').value = data['descripcion'];
        document.getElementById('colonia').value = data['colonia'];
        var date = new Date(data['fechaPropuesta']);
        var yyyy = date.getFullYear();
        var mm = String(date.getMonth() + 1).padStart(2, '0');
        var dd = String(date.getDate()).padStart(2, '0');
        document.getElementById('propuesta').value = yyyy + '-' + mm + '-' + dd;
        var date = new Date(data['fechaAcabado']);
        var yyyy = date.getFullYear();
        var mm = String(date.getMonth() + 1).padStart(2, '0');
        var dd = String(date.getDate()).padStart(2, '0');
        document.getElementById('termino').value = yyyy + '-' + mm + '-' + dd;
        document.getElementById('cuadrilla').value = data['cuadrilla'];
        document.getElementById('img').src = "/static/img/"+data['foto'];
    })
    .catch(error => console.log(error))
}

let Crear = () => {
    data = {
        id: document.getElementById('id').value,
        nombre: document.getElementById('nombre').value,
        descripcion: document.getElementById('descripcion').value,
        colonia: document.getElementById('colonia').value,
        propuesta: document.getElementById('propuesta').value,
        termino: document.getElementById('termino').value,
        cuadrilla: document.getElementById('cuadrilla').value
    };
    fetch("/crearActividad", {
        method:"POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then (response => response.json())
    .then(data => {
        console.log(data)
        if(data['estado'] == 'creado'){
            window.location.replace("/Actividades")
        }
        else{
            alert("no se pudo crear")
        }
    })
}

let Actualizar = () => {
    data = {
        id: document.getElementById('id').value,
        nombre: document.getElementById('nombre').value,
        descripcion: document.getElementById('descripcion').value,
        colonia: document.getElementById('colonia').value,
        propuesta: document.getElementById('propuesta').value,
        termino: document.getElementById('termino').value,
        cuadrilla: document.getElementById('cuadrilla').value
    };
    fetch("/actualizarActividad", {
        method:"POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then (response => response.json())
    .then(data => {
        console.log(data)
        if(data['estado'] == 'creado'){
            window.location.replace("/Actividades")
        }
        else{
            alert("no se pudo actualizar")
        }
    })
}

let Eliminar = () => {
    data = {
        id: document.getElementById('id').value,
    };
    fetch("/eliminarActividad", {
        method:"POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then (response => response.json())
    .then(data => {
        console.log(data)
        if(data['estado'] == 'creado'){
            window.location.replace("/Actividades")
        }
        else{
            alert("no se pudo eliminar")
        }
    })
}

let limpiar = () => {
    document.getElementById('id').value = "";
    document.getElementById('nombre').value = "";
    document.getElementById('descripcion').value = "";
    document.getElementById('colonia').value = "";
    document.getElementById('propuesta').value = "";
    document.getElementById('termino').value = "";
    document.getElementById('cuadrilla').value = "";
}