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


});

document.getElementById("saveBtn")
.addEventListener("click", async ()=>{
console.log("SAVE BUTTON CLICKED");

    const token = localStorage.getItem("token");

    const response = await fetch(
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

const data = await response.json();

console.log("UPDATED PROFILE:", data);
    addNotification(
    "Profile Updated",
    "Your profile was updated successfully"
);

    alert("Profile Updated");

    localStorage.setItem(
    "displayName",
    `${document.getElementById("firstName").value}
     ${document.getElementById("lastName").value}`
);
window.location.href="account.html";
});