

async function searchProducts() {

    const params = new URLSearchParams(window.location.search);

    const query = params.get("q");

    if (!query) return;

    try {

        const response = await fetch(
            `${API_BASE_URL}/products/search?q=${query}`
        );

        const products = await response.json();

        const container =
            document.querySelector(".search-results-list");

        container.innerHTML = "";

        products.forEach(product => {

            container.innerHTML += `
            <div class="product-list-row"
                 onclick="window.location.href='./product-detail.html?id=${product.product_id}'">

                <div class="product-list-img-box">
                    📦
                </div>

                <div class="product-list-details">
                    <a class="product-list-title">
                        ${product.name}
                    </a>

                    <div>
                        Rating: ${product.rating}
                    </div>

                    <div>
                        ₹${product.price}
                    </div>

                </div>

            </div>
            `;
        });

    } catch (error) {
        console.error(error);
    }
}

searchProducts();