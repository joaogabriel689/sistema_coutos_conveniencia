
document.addEventListener("DOMContentLoaded", function () {
    const categorySelect = document.getElementById("category");
    const subcategorySelect = document.getElementById("subcategory");

    const subcategories = JSON.parse(
        document.getElementById("subcategories-data").textContent
    );

    const selectedCategory = categorySelect.value;
    const selectedSubcategory = "{{ request.GET.subcategory|default:'' }}";

    function updateSubcategories(categoryId) {
        subcategorySelect.innerHTML = '<option value="">Todas</option>';

        if (!categoryId) return;

        subcategories.forEach(item => {
            if (item.fields.categoria == categoryId) {
                const option = document.createElement("option");
                option.value = item.pk;
                option.textContent = item.fields.nome;

                if (option.value === selectedSubcategory) {
                    option.selected = true;
                }

                subcategorySelect.appendChild(option);
            }
        });
    }

    // Atualiza ao mudar categoria
    categorySelect.addEventListener("change", function () {
        updateSubcategories(this.value);
    });

    // Inicializa caso já venha filtrado via GET
    if (selectedCategory) {
        updateSubcategories(selectedCategory);
    }
});

