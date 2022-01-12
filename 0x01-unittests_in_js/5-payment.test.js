const chai = require("chai");
const sinon = require("sinon")

const expect = chai.expect;

const sendPaymentRequestToApi = require("./3-payment");

describe('sendPaymentRequestToApi', () => {
    let cSpy;

    beforeEach(() => {
	cSpy = sinon.spy(console, 'log')
    })

    afterEach(() => {
	expect(cSpy.calledOnce).to.be.true
	cSpy.restore()
    })

    it('check output of sendPaymentRequestToApi', () => {
	sendPaymentRequestToApi(100, 20)

	expect(cSpy.calledWith('The total is: 120')).to.be.true
    })
    it('check output of sendPaymentRequestToApi', () => {
	sendPaymentRequestToApi(10, 10)

	expect(cSpy.calledWith('The total is: 20')).to.be.true
    })
})
