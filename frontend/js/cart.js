

async function loadCart() {

    const token = localStorage.getItem("token");

    const response = await fetch(
        `${API_BASE_URL}/cart/6`,
        {
            headers:{
                Authorization:`Bearer ${token}`
            }
        }
    );

    const items = await response.json();
    const container =
document.getElementById("cart-container");

container.innerHTML = "";

items.forEach(item => {
    container.innerHTML += `
        <div>
            Product ID: ${item.product_id}
            Quantity: ${item.quantity}
            <button onclick="removeItem(${item.cart_item_id})">
                Remove
            </button>
        </div>
    `;
});

    console.log(items);
}

async function removeItem(cartItemId){

    const token = localStorage.getItem("token");

    await fetch(
        `${API_BASE_URL}/cart/items/${cartItemId}`,
        {
            method:"DELETE",
            headers:{
                Authorization:`Bearer ${token}`
            }
        }
    );

    loadCart();
}
async function updateQty(cartItemId, qty){

    const token = localStorage.getItem("token");

    await fetch(
        `${API_BASE_URL}/cart/items/${cartItemId}`,
        {
            method:"PUT",
            headers:{
                "Content-Type":"application/json",
                Authorization:`Bearer ${token}`
            },
            body: JSON.stringify({
                quantity: qty
            })
        }
    );

    loadCart();
}

loadCart();