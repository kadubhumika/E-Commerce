const API_URL = "http://127.0.0.1:8000";

const searchInput = document.getElementById("searchInput");

if (searchInput) {
    searchInput.addEventListener("keydown", (e) => {

        if (e.key === "Enter") {
            const query = searchInput.value.trim();

            if (query) {
                window.location.href =
                    `search.html?q=${encodeURIComponent(query)}`;
            }
        }
    });
}

async function loadProducts() {

    const res = await fetch(`${API_URL}/products`);
    const products = await res.json();

    const container = document.getElementById("products-container");

    container.innerHTML = "";

    products.forEach(product => {
        container.innerHTML += `
            <div class="product-shelf-card"
                 onclick="window.location.href='./product-detail.html?id=${product.product_id}'">

                <div class="product-img-box">📦</div>

                <p>${product.name}</p>

                <strong>₹${product.price}</strong>

            </div>
        `;
    });
}

loadProducts();