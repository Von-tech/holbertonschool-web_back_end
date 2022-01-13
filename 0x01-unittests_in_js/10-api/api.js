const express = require('express');
const app = express();
const port = 7865;

app.get('/', (req, response) => response.end('Welcome to the payment system'))
app.listen(port, () => console.log(`API available on localhost port ${port}`));
app.get('/cart/:id([0-9]*)', (req, response) => response.end(`Payment methods for cart ${req.params.id}`));
app.get('/available_payments', (req, response) => {
    response.json({
	payment_methods: {
	    credit_cards: true,
	    paypal: false
	}
    })
})
app.post('/login', (req, response) => response.end(`Welcome ${req.body.userName}`));

module.exports = app;
