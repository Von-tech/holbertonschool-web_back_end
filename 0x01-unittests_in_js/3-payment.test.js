const chai = require("chai");
const sinon = require("sinon")

const expect = chai.expect;

const Utils = require('./utils');
const sendPaymentRequestToApi = require("./3-payment");

describe('sendPaymentRequestToApi', () => {
    it('We are validating our use of Utils.calculateNumber', () => {
	let cNumSpy = sinon.spy(Utils, 'calculateNumber')
	sendPaymentRequestToApi(100, 20)

	expect(cNumSpy.calledWith('SUM', 100, 20)).to.be.true
	cNumSpy.restore()
    });
})
