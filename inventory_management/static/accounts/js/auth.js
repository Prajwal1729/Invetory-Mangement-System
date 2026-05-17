$(document).ready(function () {

    // Password Regex
    let passwordPattern =
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{6,}$/;

    // =========================
    // REGISTER
    // =========================

    $('#registerForm').submit(function (e) {

        e.preventDefault();

        $('.text-danger').text('');
        $('#registerMessage').html('');

        let first_name = $('#first_name').val().trim();
        let last_name = $('#last_name').val().trim();
        let username = $('#username').val().trim();
        let email = $('#email').val().trim();
        let phone = $('#phone').val().trim();
        let role = $('#role').val();
        let password1 = $('#password1').val();
        let password2 = $('#password2').val();

        let isValid = true;

        // First Name

        if (first_name === '') {

            $('#firstNameError').text(
                'First name is required'
            );

            isValid = false;
        }

        // Last Name

        if (last_name === '') {

            $('#lastNameError').text(
                'Last name is required'
            );

            isValid = false;
        }

        // Username

        if (username === '') {

            $('#usernameError').text(
                'Username is required'
            );

            isValid = false;
        }

        // Email

        if (email === '') {

            $('#emailError').text(
                'Email is required'
            );

            isValid = false;

        } else {

            let emailPattern =
                /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailPattern.test(email)) {

                $('#emailError').text(
                    'Enter valid email'
                );

                isValid = false;
            }
        }

        // Phone

       $('#phoneError').text('');

        if (phone === '') {

            $('#phoneError').text(
                'Phone number is required'
            );

            isValid = false;

        } else if (!/^[0-9]+$/.test(phone)) {

            $('#phoneError').text(
                'Phone number must contain only digits'
            );

            isValid = false;

        } else if (phone.length !== 10) {

            $('#phoneError').text(
                'Phone number must be exactly 10 digits'
            );

            isValid = false;
        }
        // Role

        if (role === '') {

            $('#roleError').text(
                'Please select role'
            );

            isValid = false;
        }

        // Password

        if (password1 === '') {

            $('#password1Error').text(
                'Password is required'
            );

            isValid = false;

        } else if (password1.length < 6) {

            $('#password1Error').text(
                'Password must be at least 6 characters'
            );

            isValid = false;

        } else if (!passwordPattern.test(password1)) {

            $('#password1Error').text(
                'Password must contain uppercase, lowercase and special character'
            );

            isValid = false;
        }

        // Confirm Password

        if (password2 === '') {

            $('#password2Error').text(
                'Confirm password is required'
            );

            isValid = false;

        } else if (password1 !== password2) {

            $('#password2Error').text(
                'Passwords do not match'
            );

            isValid = false;
        }

        if (!isValid) {
            return;
        }

        $.ajax({

            url: '/register/',
            type: 'POST',
            data: $(this).serialize(),

            success: function (response) {

                if (response.status === 'success') {

                    $('#registerMessage').html(`
                        <div class="alert alert-success">
                            ${response.message}
                        </div>
                    `);

                    $('#registerForm')[0].reset();

                    setTimeout(() => {
                        window.location.href = '/login/';
                    }, 1500);

                } else {

                    $('#registerMessage').html(`
                        <div class="alert alert-danger">
                            Registration failed
                        </div>
                    `);
                }
            }
        });
    });


    // =========================
    // LOGIN
    // =========================

    $('#loginForm').submit(function (e) {

        e.preventDefault();

        $('#usernameError').text('');
        $('#passwordError').text('');
        $('#loginMessage').html('');

        let username =
            $('#username').val()?.trim() || '';

        let password =
            $('#password').val()?.trim() || '';

        let isValid = true;

        // Username

        if (username === '') {

            $('#usernameError').text(
                'Username is required'
            );

            isValid = false;
        }

        // Password

        if (password === '') {

            $('#passwordError').text(
                'Password is required'
            );

            isValid = false;

        } else if (password.length < 6) {

            $('#passwordError').text(
                'Password must be at least 6 characters'
            );

            isValid = false;

        } 

        if (!isValid) {
            return;
        }

        $.ajax({

            url: '/login/',
            type: 'POST',
            data: $(this).serialize(),

            success: function (response) {

                if (response.status === 'success') {

                    $('#loginMessage').html(`
                        <div class="alert alert-success">
                            ${response.message}
                        </div>
                    `);

                    setTimeout(() => {
                        window.location.href = '/dashboard/';
                    }, 1000);

                } else {

                    $('#loginMessage').html(`
                        <div class="alert alert-danger">
                            ${response.message}
                        </div>
                    `);
                }
            }
        });
    });

});