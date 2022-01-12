const chai = require("chai");
const sinon = require("sinon")

const expect = chai.expect;

const Utils = require('./utils');
const sendPaymentRequestToApi = require("./3-payment");

describe('sendPaymentRequestToApi', () => {
    it('We are validating our use of Utils.calculateNumber', () => {
	const cNumStub = sinon.stub(Utils, 'calculateNumber').returns(10)
	const cSpy = sinon.spy(console, 'log')

	sendPaymentRequestToApi(100, 20)

	expect(cNumStub.calledWith('SUM', 100, 20)).to.be.true
	expect(cNumStub.alwaysReturned(10)).to.be.true
	expect(cSpy.calledWith('The total is: 10')).to.be.true

	cNumStub.restore()
	cSpy.restore()
    });

})
