/* Messages
-------------------------------------------------- */

/* Ferme les messages d'alerte au bout de x secs */
// Bootstrap 5
// window.setTimeout(() => {
//     const alertNode = document.querySelector('.alert');
//     const alert = new bootstrap.Alert(alertNode)
//     alert.close()
// }, 3000)

// Core UI
window.setTimeout(() => {
    const alertNode = document.querySelector('.alert');
    const alert = new coreui.Alert(alertNode)
    alert.close()
}, 3000)


/* Captcha
-------------------------------------------------- */

/* Active le bouton inscription si le Captcha est coché */
function enableSubmitBtn() {
    document.getElementById("recaptcha-submit").disabled = false;
}


/* Auth
-------------------------------------------------- */
/* Log out Submit avec un click event */
function signOutLink() {
  document.getElementById("#signOutBtn").click();
}

