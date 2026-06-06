async function loadCart() {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/cart/8`, {
    headers: { Authorization: `Bearer ${token}` }
  });
  const items = await response.json();
  const container = document.getElementById("cart-container");
  container.innerHTML = "";

  items.forEach(item => {
    // 1. Fixed the dangling template literal issue
    container.innerHTML += `
      <div class="cart-product-sheet">
        <div class="cart-item-core-row">
          <div class="cart-item-img-box">
            ${item.image_url ? `<img src="${item.image_url}" width="80">` : "📦"}
          </div>
          <div class="cart-item-details">
            <h3>${item.name}</h3>
            <p>₹${item.price}</p>
            <button onclick="updateQty(${item.cart_item_id}, ${item.quantity - 1})">-</button>
            ${item.quantity}
            <button onclick="updateQty(${item.cart_item_id}, ${item.quantity + 1})">+</button>
            <button onclick="removeItem(${item.cart_item_id})">Remove</button>
          </div>
        </div>
      </div>`;
  });

  console.log(items);
}

async function removeItem(cartItemId) {
  const token = localStorage.getItem("token");
  await fetch(`${API_BASE_URL}/cart/items/${cartItemId}`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${token}` }
  });
  
  // 2. Refresh cart first, then notify
  await loadCart(); 
  addNotification("Cart Updated", "Item removed from cart");
}

async function updateQty(cartItemId, qty) {
  if (qty < 1) {
    // Proactive UX: Automatically remove the item if quantity drops below 1
    removeItem(cartItemId);
    return;
  }
  
  const token = localStorage.getItem("token");
  await fetch(`${API_BASE_URL}/cart/items/${cartItemId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify({ quantity: qty })
  });
  
  // 3. Refresh cart first, then notify
  await loadCart();
  addNotification("Cart Updated", "Quantity updated");
}

// Initial fetch on page load
loadCart();
