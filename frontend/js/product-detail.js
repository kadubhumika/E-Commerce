const API_BASE_URL = "http://127.0.0.1:8000";

async function loadProduct() {

    const params = new URLSearchParams(window.location.search);
    const productId = params.get("id");

    if (!productId) return;

    try {

        const response = await fetch(
            `${API_BASE_URL}/products/${productId}`
        );

        const product = await response.json();

        console.log(product);

        // Product Name
        document.querySelector(".detail-title").textContent =
            product.name;

        // Product Price
        document.querySelector(".new-amt").textContent =
            `₹${product.price}`;

        // Rating
        document.querySelector(".rating-count").innerHTML =
            `<strong>${product.rating || 0}</strong> Rating`;

        // Product Image
        document.querySelector(".main-display-img").innerHTML =
            product.image_url
                ? `<img src="${product.image_url}" width="300">`
                : "📦";

    } catch (error) {
        console.error(error);
    }
}

loadProduct();


document
  .getElementById("add-to-cart-btn")
  .addEventListener("click", addToCart);

async function addToCart() {

    const params = new URLSearchParams(window.location.search);
    const productId = params.get("id");

    const token = localStorage.getItem("token");

    const cartItem = {
        product_id: Number(productId),
        quantity: 1
    };

    const response = await fetch(
        `${API_BASE_URL}/cart/items`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify(cartItem)
        }
    );

    const data = await response.json();

    console.log(data);

    alert("Added to cart");
}