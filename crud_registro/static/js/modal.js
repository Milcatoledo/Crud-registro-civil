    const modalCrear = document.getElementById("modalRegistro");
    const btnCrear = document.getElementById("open_modal");
    const spanCrear = document.getElementsByClassName("close")[0];
    //Crear nuevo registro
    btnCrear.onclick = function() { 
        modalCrear.style.display = "block";
    }
    spanCrear.onclick = function() {
        modalCrear.style.display = "none";
    }
    // Editar registro
    document.querySelectorAll('.btn-update-modal').forEach(btn => {
        btn.onclick = function() {
            const modal = this.nextElementSibling; // Obtener el modal asociado al botón
            modal.style.display = "block";
            const spanUpdate = modal.querySelector('.close-update');
            spanUpdate.onclick = () => modal.style.display = "none";
        }
    })
    window.onclick = function(event) {
        if (event.target == modalCrear) {
            modalCrear.style.display = "none";
        }
    }