// /*
//     Core logic/payment flow for this comes from here:
//     https://stripe.com/docs/payments/accept-a-payment
//     CSS from here: 
//     https://stripe.com/docs/stripe-js
// */
// //create stripe element
// var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
// var stripe = Stripe(stripePublicKey);

// //create an instance of the element
// var elements = stripe.elements();
// var style = {
//     base: {
//         color: '#000',
//         fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
//         fontSmoothing: 'antialiased',
//         fontSize: '16px',
//         '::placeholder': {
//             color: '#aab7c4'
//         }
//     },
//     invalid: {
//         color: '#dc3545',
//         iconColor: '#dc3545'
//     }
// };

// //create an instance of the card Element
// var card = elements.create('card', {style: style});
// //add an instance of the card 
// card.mount('#card-element');
// // Handle realtime validation errors on the card element
// card.addEventListener('change', function (event) {
//     var errorDiv = document.getElementById('card-errors');
//     if (event.error) {
//         var html = `
//             <span class="icon" role="alert">
//                 <i class="fas fa-times"></i>
//             </span>
//             <span>${event.error.message}</span>
//         `;
//         $(errorDiv).html(html);
//     } else {
//         errorDiv.textContent = '';
//     }
// });

// // Handle form submit
// var form = document.getElementById('payment-form');
// form.addEventListener('submit', function(event) {
//     event.preventDefault();
    
//     stripe.createToken(card).then(function(result){
//         if(result.error){
//             //inform user if they have an error.
//             varerrorElement = document.getElementById('card-errors');
//             errorElement.textContent = result.error.message;
//         }else{
//             //send token to server
//             stripeTokenHandler(result.Token);
//         }
//     });
// });

// //submit the form with the TokenID 

// function stripeTokenHandler(token){
//     //insert the token ID into the form so it gets submiutted to the server.
//     var form = document.getElementById('payment-form');
//     var hiddenInput  = document.createElement('input');
//     hiddenInput.setAttribute('type', 'hidden');
//     hiddenInput.setAttribute('name', 'stripeToken');
//     hiddenInput.setAttribute('value', token.id);
//     form.appendChild(hiddenInput);
//     form.submit();
// }

const stripe = Stripe("pk_test_51KpZBDIaE0NFUuueBYiW9whBxPp9gNq5VDqAJztk6gqjwAIvhGp6SoAJJqbNTThnOqJ0nn0ggEQnjnOcNTbCBkpk00M0XbQDYX");
const elem = document.getElementById('submit-button');
let clientSecret = elem.getAttribute('data-secret');

var elements = stripe.elements();
var style = {
base: {
  color: "#000",
  lineHeight: '2.4',
  fontSize: '16px'
}
};

// mount card element
var card = elements.create("card", { hidePostalCode: true, style: style });
card.mount("#card-element");

card.on('change', ({error}) => {
  let displayError = document.getElementById('card-errors');
  if (error) {
    displayError.textContent = error.message;
  } else {
    displayError.textContent = '';
  }
});


var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  document.querySelector('#cancel-btn').classList.add('d-none');
  elem.classList.add('d-none');
  document.querySelector('.loader').classList.remove('d-none');

  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function(result) {
    if (result.error) {
    console.log(result.error.message);
      // add a failed page here
      // window.location.replace('/')
    } else {
      // The payment has been processed!
      if (result.paymentIntent.status === 'succeeded') {
        console.log('payment processed');
        window.location.replace(checkoutCompleteUrl);
        // Show a success message to your customer
        // There's a risk of the customer closing the window before callback
        // execution. Set up a webhook or plugin to listen for the
        // payment_intent.succeeded event that handles any business critical
        // post-payment actions.
      }
    }
  })
  })

