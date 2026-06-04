document.addEventListener("DOMContentLoaded", async () => {

    const token = localStorage.getItem("token");

    try {

        const response = await fetch(
            `${API_BASE_URL}/orders/my-orders`,
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        );

        const data = await response.json();

        console.log("Orders:", data);

    } catch (error) {
        console.log(error);
    }

});