const username = "admin";
const password = "admin";

const userNameInput = document.querySelector("#username");
const passwordInput = document.querySelector("#password");
const loginButton = document.querySelector("#loginButton");

loginButton.addEventListener("click", function(event) {
    event.preventDefault(); // Prevent form submission
    
    const userinput = userNameInput.value;
    const passinput = passwordInput.value;

    if (userinput === username && passinput === password) {
        window.location.href = "mainpage.html";
    } else {
        alert("Invalid username or password");
    }
});