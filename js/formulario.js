// formulario.js

document.addEventListener('DOMContentLoaded', () => {
    const tipoResiduoSelect = document.getElementById('tipoResiduo');
    const subcategoriaSelect = document.getElementById('subcategoria');

    // Definir las subcategorías para cada tipo de residuo
    const subcategorias = {
        plastico: ['Botellas', 'Envases', 'Bolsas'],
        papel: ['Periódicos', 'Revistas', 'Cartón'],
        vidrio: ['Botellas', 'Tarros', 'Frascos'],
        metales: ['Latas', 'Cajas de metal', 'Otros metales'],
        electronicos: ['Computadoras', 'Teléfonos', 'Electrodomésticos']
    };

    // Actualizar subcategorías cuando cambia el tipo de residuo
    tipoResiduoSelect.addEventListener('change', () => {
        const tipoSeleccionado = tipoResiduoSelect.value;
        subcategoriaSelect.innerHTML = '<option value="">Seleccionar...</option>'; // Limpiar las opciones anteriores

        if (tipoSeleccionado && subcategorias[tipoSeleccionado]) {
            subcategorias[tipoSeleccionado].forEach(subcategoria => {
                const option = document.createElement('option');
                option.value = subcategoria.toLowerCase().replace(/ /g, '_');
                option.textContent = subcategoria;
                subcategoriaSelect.appendChild(option);
            });
        }
    });

    // Manejar el envío del formulario
    recyclingForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevenir el envío real del formulario

        // Mostrar el mensaje de confirmación como un pop-up
        alert('Solicitud de recolección ingresada correctamente. ¡Gracias!');

        // Limpiar los campos del formulario
        recyclingForm.reset();

        // Opcional: limpiar las subcategorías
        subcategoriaSelect.innerHTML = '<option value="">Seleccionar...</option>';

        // Opcional: restablecer el tipo de residuo a la opción predeterminada
        tipoResiduoSelect.selectedIndex = 0;

        // Aquí puedes agregar código para enviar los datos del formulario a un servidor si es necesario
    });
});
