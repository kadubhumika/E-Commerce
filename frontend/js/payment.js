document
.getElementById("payBtn")
.addEventListener("click", async () => {

    const token =
        localStorage.getItem("token");

    const customerId =
        localStorage.getItem("customer_id");

    const response = await fetch(
        `${API_BASE_URL}/orders/checkout/${customerId}?payment_method=UPI`,
        {
            method: "POST",
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    const order = await response.json();

    addNotification(
        "Order Placed",
        "Your order was placed successfully"
    );

    localStorage.setItem(
        "latest_order_id",
        order.order_id
    );

    alert("Payment Successful");

    window.location.href = "order.html";
});