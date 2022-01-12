const chai = require("chai");
const sinon = require("sinon");

const expect = chai.expect;

const getPaymentTokenFromApi = require("./6-payment_token");

describe('getPaymentTokenFromApi', function () {
    it('Test the reult of the function where true is success', function(done) {
	getPaymentTokenFromApi(true).then(function(response) {
	    expect(response.data).to.equal('Successful response from the API');
	    done();
	});
    });
});
