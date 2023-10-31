document.getElementById('signUpLink').addEventListener('click', function () {
    // Open the modal
    var modal = new bootstrap.Modal(document.getElementById('modalRegisterForm'));
    modal.show();
  });
  
  document.getElementById('loginLink').addEventListener('click', function () {
    // Open the modal
    var modal = new bootstrap.Modal(document.getElementById('modalLoginForm'));
    modal.show();
  });