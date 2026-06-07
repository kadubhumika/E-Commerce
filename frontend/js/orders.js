async function loadOrders() {

    const token = localStorage.getItem("token");

    const response = await fetch(
        `${API_BASE_URL}/orders/my-orders`,
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    const orders = await response.json();

    console.log("Orders:", orders);

    const container =
        document.getElementById("orders-container");

    container.innerHTML = "";

    if (orders.length === 0) {
        container.innerHTML = `
            <h2>No Orders Yet</h2>
        `;
        return;
    }

    orders.forEach(order => {

        container.innerHTML += `

        <div class="order-tracking-card">

            <div class="order-item-thumb">
                📦
            </div>

            <div class="order-item-info">
                <h3>Order #${order.order_id}</h3>

                <p>${order.shipping_address}</p>

                <p style="
                    margin-top:6px;
                    font-weight:700;
                    color:var(--glint-yellow);
                ">
                    ₹${order.total_amount}
                </p>

                <p>
                    Payment :
                    ${order.payment_method}
                </p>

                <p>
                    Status :
                    ${order.status}
                </p>
            </div>

        </div>

        `;
    });
}

loadOrders();