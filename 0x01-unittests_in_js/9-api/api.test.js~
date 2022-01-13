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
    });
})
