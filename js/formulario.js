

document.addEventListener('DOMContentLoaded', () => {
    const tipoResiduoSelect = document.getElementById('tipoResiduo');
    const subcategoriaSelect = document.getElementById('subcategoria');

    // definir las subcategorías para cada tipo de residuo
    const subcategorias = {
        plastico: ['Botellas', 'Envases', 'Bolsas'],
        papel: ['Periódicos', 'Revistas', 'Cartón'],
        vidrio: ['Botellas', 'Tarros', 'Frascos'],
        metales: ['Latas', 'Cajas de metal', 'Otros metales'],
        electronicos: ['Computadoras', 'Teléfonos', 'Electrodomésticos']
    };

    // actualizar subcategorías cuando cambia el tipo de residuo
    tipoResiduoSelect.addEventListener('change', () => {
        const tipoSeleccionado = tipoResiduoSelect.value;
        subcategoriaSelect.innerHTML = '<option value="">Seleccionar...</option>'; // limpiar las opciones anteriores

        if (tipoSeleccionado && subcategorias[tipoSeleccionado]) {
            subcategorias[tipoSeleccionado].forEach(subcategoria => {
                const option = document.createElement('option');
                option.value = subcategoria.toLowerCase().replace(/ /g, '_');
                option.textContent = subcategoria;
                subcategoriaSelect.appendChild(option);
            });
        }
    });

    // envío del formulario
    recyclingForm.addEventListener('submit', (event) => {
        event.preventDefault(); 

        alert('Solicitud de recolección ingresada correctamente. ¡Gracias!');

        recyclingForm.reset();

        subcategoriaSelect.innerHTML = '<option value="">Seleccionar...</option>';

        tipoResiduoSelect.selectedIndex = 0;

    });
});
