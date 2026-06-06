document.addEventListener("DOMContentLoaded", async () => {

    const token = localStorage.getItem("token");

    const response = await fetch(
        `${API_BASE_URL}/profile`,
        {
            headers:{
                Authorization:`Bearer ${token}`
            }
        }
    );

    const profile = await response.json();

    document.getElementById("firstName").value =
        profile.first_name || "";

    document.getElementById("lastName").value =
        profile.last_name || "";

    document.getElementById("phone").value =
        profile.phone || "";

    document.getElementById("email").value =
        profile.email || "";
});

document.getElementById("saveBtn")
.addEventListener("click", async ()=>{

    const token = localStorage.getItem("token");

    await fetch(
        `${API_BASE_URL}/profile`,
        {
            method:"PUT",
            headers:{
                "Content-Type":"application/json",
                Authorization:`Bearer ${token}`
            },
            body:JSON.stringify({
                first_name:
                    document.getElementById("firstName").value,

                last_name:
                    document.getElementById("lastName").value,

                phone:
                    document.getElementById("phone").value
            })
        }
    );
    addNotification(
    "Profile Updated",
    "Your profile was updated successfully"
);

    alert("Profile Updated");

    window.location.href="account.html";
});