document.addEventListener("DOMContentLoaded", function () {
    let isLoggedIn = false; 
    let username = ""; 

    let buttonContainer = document.querySelector(".menu div");
    
    if (isLoggedIn) {
        alert("Logged in successfully!");
        buttonContainer.innerHTML = `
            <span class="username">Welcome, ${username}</span>
            <button class="button" onclick="logout()">Logout</button>
        `;
    } else {
        alert("Logged out successfully!");
        buttonContainer.innerHTML = `
            <button class="button" onclick="window.location.href='/login';">Login</button>
        `;
    }
});
