function myFunction() {
  document.location.href = 'homepage.html';
  }
  const setupUI = (user) => {
    if (user) {
      window.location.href = "index.html";
      };
  
    } 
  // login
  const loginForm = document.querySelector('#login-form');
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // get user information
    const email = loginForm['login-email'].value;
    const password = loginForm['login-password'].value;
  
    // log the user in
    firebase.auth().signInWithEmailAndPassword(email, password).then((cred) => {
      myFunction();
      
    }).catch(function(error) {
      var errorCode = error.code;
      var errorMessage = error.message;
  
      // User not found? Create user.
      if ( errorCode === 'auth/user-not-found' ) {
          alert('User not found');
    
      // Wrong Password Error
      } else if ( errorCode === 'auth/wrong-password' ) {
          
          alert('Wrong password. Please try again');
      } else {
          alert( errorMessage );
      }
      console.log( error );
  });
  
  });