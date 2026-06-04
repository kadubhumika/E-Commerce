document.addEventListener("DOMContentLoaded", async () => {

    const token = localStorage.getItem("token");

    if (!token) {
        window.location.href = "login.html";
        return;
    }

    try {

        const response = await fetch(
            `${API_BASE_URL}/products`
        );

        const products = await response.json();

        console.log("Products:", products);

        const productGrid =
            document.querySelector(".product-web-grid");

        productGrid.innerHTML = "";

        products.forEach(product => {

            productGrid.innerHTML += `
                <div class="product-shelf-card">
                    <div class="product-img-box">📦</div>
                    <p>${product.name}</p>
                    <span>${product.price}</span>
                </div>
            `;

        });

    }
    catch (error) {
        console.error(error);
    }

});