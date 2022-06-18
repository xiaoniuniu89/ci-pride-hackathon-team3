/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/
//create stripe element
var stripePublicKey = ('pk_test_k00xao0P5r64RAYcBGuR9enF002XDNTq52');
var stripe = Stripe(stripePublicKey);

//create an instance of the element
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

//create an instance of the card Element
var card = elements.create('card', {style: style});
//add an instance of the card 
card.mount('#card-element');
// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    
    stripe.createToken(card).then(function(result){
        if(result.error){
            //inform user if they have an error.
            varerrorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        }else{
            //send token to server
            stripeTokenHandler(result.Token);
        }
    });
});

//submit the form with the TokenID 

function stripeTokenHandler(token){
    //insert the token ID into the form so it gets submiutted to the server.
    var form = document.getElementById('payment-form');
    var hiddenInput  = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', token.id);
    form.appendChild(hiddenInput);
    form.submit();
}




