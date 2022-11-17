
// function to show password
function showPassword() {

    let x = document.getElementById("password");

    if ( x.type == "password") {

        x.type = "text";
    } else {

        x.type = "password";
    }
}


// remove flashedMessage
function removeFlash() {

    let x = document.querySelector("#e-message-container > div");

    setTimeout(() => {
        x.remove()
    }, 3000)
}


// remove flashedMessage
const dayClicked = (element) => {
    window.location ="/devo" + "?date=" + element.id
}