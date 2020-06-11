function checkForm(form)
  	{
    	if(!form.terms.checked) 
		{
      		alert("You have to agree to the terms and conditions to proceed");
      		return false;
    	}
	return true;
	}

function viewPassword()
{
  var passwordInput = document.getElementById('password-field');
  var passStatus = document.getElementById('pass-status');
 
  if (passwordInput.type == 'password'){
    passwordInput.type='text';
    passStatus.className='fa fa-eye-slash';
    
  }
  else{
    passwordInput.type='password';
    passStatus.className='fa fa-eye';
  }
}

