// sign up
var value = $("#password_reg").val();
$.validator.addMethod("checklower", function (value) {
    return /[a-z]/.test(value);
});
$.validator.addMethod("checkupper", function (value) {
    return /[A-Z]/.test(value);
});
$.validator.addMethod("checkdigit", function (value) {
    return /[0-9]/.test(value);
});
$.validator.addMethod("pwcheck", function (value) {
    return /^[A-Za-z0-9\d=!\-@._*]*$/.test(value) && /[a-z]/.test(value) && /\d/.test(value) && /[A-Z]/.test(value);
});

$('#signup').validate({
    errorClass: 'errors',
    rules: {
        first_name: {
            required: true,
            maxlength:30
        },
        phone: {
            required: true,
            phoneUS: true
            

        },
        email: {
            required: true,
            email: true,
        },
        place:{
            required: true,
        },
        password: {
            minlength: 8,
            maxlength: 30,
            required: true,
            //pwcheck: true,
            checklower: true,
            checkupper: true,
            checkdigit: true

        },
        confirm_password: {
            required: true,
            equalTo: "#password_reg",
        },
        
    },
    messages: {
        first_name: {
            required: "Please enter first name",
        },
        email: {
            required: "Please enter email address",
            email: "Enter a valid email"

        },
        password: {
            pwcheck: "Password is not strong enough",
            checklower: "Need atleast 1 lowercase alphabet",
            checkupper: "Need atleast 1 uppercase alphabet",
            checkdigit: "Need atleast 1 digit"
        },
        confirm_password: {
            equalTo: "Password must be same"
        },
        ckeck :{
            required:"You must check Terms and conditions"
        }
    },
    submitHandler: function (form) {
        console.log('test');
        form.submit();
    
    }
})
