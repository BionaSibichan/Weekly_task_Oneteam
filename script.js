let button = document.getElementById("startButton");

button.addEventListener("click", function() {

    document.getElementById("alertMessage").innerHTML =
        "Thank you for visiting our website!";

});


let form = document.getElementById("contactForm");

form.addEventListener("submit", function(event) {

    event.preventDefault();

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;

    if (name == "" || email == "" || message == "") {

        document.getElementById("formMessage").innerHTML =
            "Please fill all the fields.";

        document.getElementById("formMessage").style.color = "red";

    } else {

        document.getElementById("formMessage").innerHTML =
            "Message sent successfully!";

        document.getElementById("formMessage").style.color = "green";

        form.reset();
    }

});