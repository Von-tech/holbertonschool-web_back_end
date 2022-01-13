const chai = require("chai");
const request = require('request');

const expect = chai.expect;

describe('Suite for the index page', () => {
    describe('GET /', () => {
	it('endpoint: checking output of GET /', (done) => {
	    request('http://localhost:7865/', (err, response, body) => {
		expect(response.statusCode).to.equal(200)
		expect(body).to.equal('Welcome to the payment system')
		done();
	    });
	});
    })
    describe('GET /cart/:id', () => {
	it('output check: GET /cart/:id', (done) => {
	    request('http://localhost:7865/cart/12', (error, response, body) => {
		expect(response.statusCode).to.equal(200)
		expect(body).to.equal('Payment methods for cart 12')
		done();
	    });
	});
    })
    describe('GET /cart/:id with id hello', () => {
	it('output check: GET /cart/hello', (done) => {
	    request('http://localhost:7865/cart/hello', (error, response, body) => {
		if (response) {
		    expect(response.statusCode).to.equal(404)
		}
		done();
	    });
	});
    });
})
