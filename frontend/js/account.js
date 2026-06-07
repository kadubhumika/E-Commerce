document.addEventListener("DOMContentLoaded", async () => {

    const token = localStorage.getItem("token");

    if (!token) {
        window.location.href = "login.html";
        return;
    }

    try {

        const response = await fetch(
            `${API_BASE_URL}/profile`,
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        );

        const profile = await response.json();
        localStorage.setItem(
    "customer_id",
    profile.customer_id
);

        console.log(profile);

        document.querySelector(
            ".profile-info-block h2"
        ).innerText =
            `Hey! ${profile.first_name}  ${profile.last_name}`;

    } catch (error) {

        console.error(error);

    }

});