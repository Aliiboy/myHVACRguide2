/* Messages
-------------------------------------------------- */

/* Ferme les messages d'alerte au bout de x secs */
window.setTimeout(() => {
    const alertNode = document.querySelector('.alert');
    const alert = new bootstrap.Alert(alertNode)
    alert.close()
}, 3000)



/* Captcha
-------------------------------------------------- */

/* Active le bouton inscription si le Captcha est coché */
function enableSubmitBtn() {
    document.getElementById("recaptcha-submit").disabled = false;
}
