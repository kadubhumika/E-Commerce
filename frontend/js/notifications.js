// Function to save a new notification to localStorage
function addNotification(title, message) {
    const notifications = JSON.parse(localStorage.getItem("notifications")) || [];

    notifications.unshift({
        title,
        message,
        time: new Date().toLocaleString()
    });

    localStorage.setItem("notifications", JSON.stringify(notifications));
}

// Function to pull notifications from localStorage and render them on the page
document.addEventListener("DOMContentLoaded", () => {
    const notifications = JSON.parse(localStorage.getItem("notifications")) || [];
    const container = document.getElementById("notificationsContainer");

    // Safety check to ensure the container exists on the current page
    if (!container) return;

    // If there are no notifications yet, show a clean empty state
    if (notifications.length === 0) {
        container.innerHTML = `
            <div style="text-align: center; padding: 40px; color: #888;">
                <p>No recent activity notifications.</p>
            </div>`;
        return;
    }

    container.innerHTML = "";

    notifications.forEach(n => {
        container.innerHTML += `
        <div class="notification-individual-card">
            <!-- Used FontAwesome icon matching your layout style -->
            <div class="notification-icon-indicator" style="color: #4ade80;">
                <i class="fa-solid fa-circle-check"></i>
            </div>

            <div class="notification-text-details">
                <h3>${n.title}</h3>
                <p>${n.message}</p>
                <span class="notification-timestamp">
                    ${n.time}
                </span>
            </div>
            <div class="notification-thumbnail-box">🛒</div>
        </div>
        `;
    });
});
