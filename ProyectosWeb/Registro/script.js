const formulario = document.getElementById("formularioRegistro");

formulario.addEventListener("submit", function(evento) {

    evento.preventDefault();

    const nombre = document.getElementById("nombre").value;

    const correo = document.getElementById("correo").value;

    const interes = document.querySelector(
        'input[name="interes"]:checked'
    ).value;

    const experiencia = document.getElementById("experiencia").value;

    const suscripcion = document.getElementById("suscripcion").checked;

    let mensajeSuscripcion;

    if (suscripcion) {
        mensajeSuscripcion = "Sí";
    } else {
        mensajeSuscripcion = "No";
    }

    const confirmacion = document.getElementById("confirmacion");

    confirmacion.innerHTML =
        "<strong>¡Registro realizado correctamente!</strong><br><br>" +
        "Nombre: " + nombre + "<br>" +
        "Correo electrónico: " + correo + "<br>" +
        "Área de interés: " + interes + "<br>" +
        "Nivel de experiencia: " + experiencia + "<br>" +
        "Suscripción al boletín: " + mensajeSuscripcion;

    confirmacion.style.display = "block";
});