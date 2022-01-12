const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber() tests", function () {
    it("return 4 from 1 and 3", function () {
	assert.equal(calculateNumber(1, 3), 4);
	});
    it("return 5 from 1 and 3.7", function () {
	assert.equal(calculateNumber(1, 3.7), 5);
	});
    it("return 5 from 1.2 and 3.7", function () {
	assert.equal(calculateNumber(1.2, 3.7), 5);
	});
    it("return 6 from 1.5 and 3.7", function () {
	assert.equal(calculateNumber(1.5, 3.7), 6);
	});
    it("return 0 from 0.1 and 0.3", function () {
	assert.equal(calculateNumber(0.1, 0.3), 0);
	});
    it("return 0 from -0.7 and 0.7", function () {
	assert.equal(calculateNumber(-0.7, 0.7), 0);
	});
    it("return -2 from -0.8 and -0.7", function () {
	assert.equal(calculateNumber(-0.8, -0.7), -2);
	});
});
// adding two digits
