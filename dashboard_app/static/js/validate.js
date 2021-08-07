/* function validateRegistration() {
    valid = true
    if (document.registration.first_name.value == "") {
        document.getElementById("err_fname").innerHTML = "Enter First Name";
        document.registration.first_name.focus();
        valid = false
    } else {
        document.getElementById("err_fname").innerHTML = "";
    }
    if (document.registration.last_name.value == "") {
        document.getElementById("err_lname").innerHTML = "Enter Last Name";
        document.registration.last_name.focus();
        valid = false
    } else {
        document.getElementById("err_lname").innerHTML = "";
    }

    if (document.registration.email.value == "") {
        document.getElementById("err_email").innerHTML = "Enter E-mail address";
        document.registration.email.focus();
        valid = false
    } else {
        document.getElementById("err_email").innerHTML = "";
    }
    if (document.registration.password.value == "") {
        document.getElementById("err_password").innerHTML = "Enter Password";
        document.registration.password.focus();
        valid = false
    } else {
        document.getElementById("err_password").innerHTML = "";
    }
    if (valid == false) {
        return false;
    } else {
        valid = true
        return true
    }
} */

$(document).ready(function() {
    $("#registration input[name='email']").keyup(function() {
        var email = $(this).val();
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
            }
        });
        $.ajax({
            url: 'validate',
            method: 'POST',
            data: {
                'email': email
            },
            dataType: 'json',
            success: function(data) {
                if (data.taken) {
                    $("#err_email").html("E-Mail is taken");
                } else {
                    $("#err_email").html("E-Mail is available");
                }
            }
        });
    });
    $('#register').click(function() {
        valid = true
        if ($("#registration input[name='first_name']").val() == "") {
            $("#err_fname").html("Enter First Name");
            valid = false
        } else {
            $("#err_fname").html("");
        }
        if ($("#registration input[name='last_name']").val() == "") {
            $("#err_lname").html("Enter Last Name");
            valid = false
        } else {
            $("#err_lname").html("");
        }
        if ($("#registration input[name='email']").val() == "") {
            $("#err_email").html("Enter E-mail");
            valid = false
        } else {
            $("#err_email").html("");
        }
        if ($("#registration input[name='password']").val() == "") {
            $("#err_password").html("Enter Password");
            valid = false
        } else {
            $("#err_password").html("");
        }
        if (valid == false) {
            return false;
        } else {
            valid = true
            return true
        }
    });
});