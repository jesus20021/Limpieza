let validacion = () => {
    let usuario = document.getElementById("usuario").value;
    let pass = document.getElementById("pass").value;
    if(usuario.length==0){
        alert("El usuario no puede ir vacio");
        return false;
    }
    else if(pass.length==0){
        alert("La contraseña no puede ir vacia");
        return false;
    }
    else{
        return true;
    }
}