/* Messages
-------------------------------------------------- */

/* Ferme les messages d'alerte au bout de x secs */
// Bootstrap 5
// window.setTimeout(() => {
//     const alertNode = document.querySelector('.alert');
//     const alert = new bootstrap.Alert(alertNode)
//     alert.close()
// }, 3000)

/* Ferme les messages d'alerte au bout de x secs */
// Core UI
window.setTimeout(() => {
    const alertNode = document.querySelector('.alert-dismissible');
    const alert = new coreui.Alert(alertNode)
    alert.close()
}, 3000)


/* Form
------------------------------------------------- */
// Example starter JavaScript for disabling form submissions if there are invalid fields
window.addEventListener('load', function () {
    // Get the forms we want to add validation styles to

  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    });
}, false);


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

