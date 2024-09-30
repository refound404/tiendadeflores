document.addEventListener("DOMContentLoaded", function () {
    const formAgregar = document.querySelector("form[action='/agregar']");
    
    formAgregar.addEventListener("submit", function (event) {
        const nombre = formAgregar.querySelector("input[name='nombre']").value.trim();
        const cantidad = formAgregar.querySelector("input[name='cantidad']").value;
        
        if (nombre === "" || cantidad <= 0) {
            alert("Por favor, complete correctamente el formulario.");
            event.preventDefault();
        }
    });
});
