window.onscroll = function() {stickyNavbar()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function stickyNavbar() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky");
    } else {
        navbar.classList.remove("sticky");
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const signupForm = document.getElementById("signupForm");

    signupForm.addEventListener("submit", function(event) {
        event.preventDefault();
        validateForm();
    });

    function validateForm() {
        const usernameInput = document.getElementById("username");
        const passwordInput = document.getElementById("password");
        const dobInput = document.getElementById("dob");
        const usernameError = document.getElementById("usernameError");
        const passwordError = document.getElementById("passwordError");
        const dobError = document.getElementById("dobError");

        // Reset errors
        usernameError.textContent = "";
        passwordError.textContent = "";
        dobError.textContent = "";

        let isValid = true;

        // Username validation
        if (usernameInput.value.trim() === "") {
            usernameError.textContent = "Username is required";
            isValid = false;
        }

        // Password validation
        if (passwordInput.value.trim() === "") {
            passwordError.textContent = "Password is required";
            isValid = false;
        }

        // Date of Birth validation
        if (dobInput.value === "") {
            dobError.textContent = "Date of Birth is required";
            isValid = false;
        }

        // If form is valid, submit it
        if (isValid) {
            alert("Signup successful!");
            signupForm.reset(); // Reset form
        }
    }
});
    