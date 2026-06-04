document.addEventListener("DOMContentLoaded", async () => {

    try {

        const response = await fetch(
            `${API_BASE_URL}/categories`
        );

        const categories = await response.json();

        console.log(categories);

        const grid =
            document.querySelector(".master-categories-grid");

        grid.innerHTML = "";

        categories.forEach(category => {

            grid.innerHTML += `
                <a href="#" class="category-grid-item">
                    <div class="large-circle-bubble">📦</div>
                    <p>${category.name}</p>
                </a>
            `;

        });

    } catch (error) {

        console.error(error);

    }

});