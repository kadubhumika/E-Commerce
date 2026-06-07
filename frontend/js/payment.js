document
.getElementById("payBtn")
.addEventListener("click", async () => {

    const upiId =
        document.getElementById("upiInput").value.trim();

    if (!upiId) {
        alert("Please enter your UPI ID");
        return;
    }

    const token =
        localStorage.getItem("token");

    const customerId =
        localStorage.getItem("customer_id");

    console.log("Customer ID:", customerId);

    if (!customerId) {
        alert("Customer ID not found");
        return;
    }

    const response = await fetch(
        `${API_BASE_URL}/orders/checkout/${customerId}?payment_method=UPI`,
        {
            method: "POST",
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    const data = await response.json();

    console.log(data);

    if (!response.ok) {
        alert(data.detail || "Order failed");
        return;
    }

    alert("Payment Successful");

    window.location.href = "order.html";
});