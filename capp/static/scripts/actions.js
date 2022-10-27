
// function to show password
function showPassword() {

    let x = document.getElementById("password");

    if ( x.type == "password") {

        x.type = "text";
    } else {

        x.type = "password";
    }
}