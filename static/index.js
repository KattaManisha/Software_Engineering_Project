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

document.addEventListener('DOMContentLoaded', function () {
  // Function to open the signup modal
  function openSignupModal() {
    var modal = new bootstrap.Modal(
      document.getElementById('modalRegisterForm')
    );
    modal.show();
  }

  // Function to open the login modal
  function openLoginModal() {
    var modal = new bootstrap.Modal(document.getElementById('modalLoginForm'));
    modal.show();
  }

  var logoutButton = document.getElementById('logoutBtn');
  if (logoutButton) {
    logoutButton.addEventListener('click', function () {
      // Perform the logout action here, e.g., by redirecting to a logout endpoint
      window.location.href = '/logout';
    });
  }

  // Attach click event listeners to the signup and login links
  var signUpLink = document.getElementById('signUpLink');
  var loginLink = document.getElementById('loginLink');

  if (signUpLink) {
    signUpLink.addEventListener('click', openSignupModal);
  }

  if (loginLink) {
    loginLink.addEventListener('click', openLoginModal);
  }

  // Function to register a new user
  function registerUser() {
    var username = document.getElementById('orangeForm-username').value;
    var first_name = document.getElementById('orangeForm-firstname').value;
    var last_name = document.getElementById('orangeForm-lastname').value;
    var email = document.getElementById('orangeForm-email').value;
    var password = document.getElementById('orangeForm-pass').value;

    var data = {
      username: username,
      first_name: first_name,
      last_name: last_name,
      email: email,
      password: password,
    };

    fetch('/register', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
        // You can update the UI or perform other actions here.
        // For now, let's display the response in the registrationResponse div.
        var registrationResponse = document.getElementById(
          'registrationResponse'
        );
        if (registrationResponse) {
          registrationResponse.innerHTML = data;
        }

        // Check if registration was successful and redirect
        if (data.includes('successful')) {
          window.location.href = '/user-home'; // Adjust the URL as needed
        }
      });
  }

  // Function to log in a user
  function loginUser() {
    var email = document.getElementById('orangeForm-email').value;
    var password = document.getElementById('orangeForm-pass').value;

    var data = {
      email: email,
      password: password,
    };

    fetch('/login', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
        // You can update the UI or perform other actions here.
        // For now, let's display the response in the loginResponse div.
        var loginResponse = document.getElementById('loginResponse');
        if (loginResponse) {
          loginResponse.innerHTML = data;
        }
        // Check if login was successful and redirect
        if (data.includes('successful')) {
          window.location.href = '/user-home'; // Adjust the URL as needed
        }
      });
  }

  // Attach click event listeners to the signup and login buttons
  var signupButton = document.getElementById('signupButton');
  var loginButton = document.getElementById('loginButton');

  if (signupButton) {
    signupButton.addEventListener('click', registerUser);
  }

  if (loginButton) {
    loginButton.addEventListener('click', loginUser);
  }
});
