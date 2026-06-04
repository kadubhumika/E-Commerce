document.addEventListener("DOMContentLoaded", async () => {

    const token = localStorage.getItem("token");

    try {

        const response = await fetch(
            `${API_BASE_URL}/cart/1`,
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        );

        const data = await response.json();

        console.log("Cart:", data);

    } catch (error) {
        console.log(error);
    }

});