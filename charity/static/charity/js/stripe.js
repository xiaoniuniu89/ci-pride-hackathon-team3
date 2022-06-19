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

