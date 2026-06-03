// =======================
// REGISTER
// =======================

const signupForm = document.getElementById("signupForm");

if (signupForm) {

    signupForm.addEventListener("submit", async (e) => {

        e.preventDefault();

        const userData = {
            username: document.getElementById("username").value,
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        };

        try {

            const response = await fetch(
                `${API_BASE_URL}/auth/register`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(userData)
                }
            );

            const data = await response.json();

            if (response.ok) {

                alert("Registration Successful");

                window.location.href =
                    "login.html";

            } else {

                alert(data.detail);

            }

        } catch (error) {

            console.log(error);

            alert("Server Error");

        }

    });

}


// =======================
// LOGIN
// =======================

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", async (e) => {

        e.preventDefault();

        const formData = new FormData();

        formData.append(
            "username",
            document.getElementById("email").value
        );

        formData.append(
            "password",
            document.getElementById("password").value
        );

        try {

            const response = await fetch(
                `${API_BASE_URL}/auth/login`,
                {
                    method: "POST",
                    body: formData
                }
            );

            const data = await response.json();

            if (response.ok) {

                localStorage.setItem(
                    "token",
                    data.access_token
                );

                window.location.href =
                    "dashboard.html";

            } else {

                alert("Invalid Credentials");

            }

        } catch (error) {

            console.log(error);

            alert("Server Error");

        }

    });

}