const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("calculateNumber() tests with type SUM", function () {
    it("return 4 from 1 and 3", function () {
	assert.equal(calculateNumber('SUM', 1, 3), 4);
    });
    it("return 5 from 1 and 3.7", function () {
	assert.equal(calculateNumber('SUM', 1, 3.7), 5);
    });
    it("return 6 from 1.5 and 3.7", function () {
	assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
    });
    it("return 0 from -0.7 and 0.7", function () {
	assert.equal(calculateNumber('SUM', -0.7, 0.7), 0);
    });
    it("return -2 from -0.8 and -0.7", function () {
	assert.equal(calculateNumber('SUM', -0.8, -0.7), -2);
    });
});

describe("calculateNumber() tests with type SUBTRACT", function () {
    it("return -4 from 1.4 and 4.5", function () {
	assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it("return -3 from 1.2 and 3.7", function () {
	assert.equal(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
    });
    it("return -2 from 1.5 and 3.7", function () {
	assert.equal(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
    });
    it("return 0 from 0.1 and 0.3", function () {
	assert.equal(calculateNumber('SUBTRACT', 0.1, 0.3), 0);
    });
    it("return 1 from 0.8 and -0.4", function () {
	assert.equal(calculateNumber('SUBTRACT', 0.8, -0.4), 1);
    });
});

describe("calculateNumber() tests with type DIVIDE", function () {
    it("return 0.25 from 1 and 4", function () {
	assert.equal(calculateNumber('DIVIDE', 1, 4), 0.25);
    });
    it("return 0.25 from 1 and 3.7", function () {
	assert.equal(calculateNumber('DIVIDE', 1, 3.7), 0.25);
    });
    it("return 'Error' from 1.3 and 0.3", function () {
	assert.equal(calculateNumber('DIVIDE', 1.3, 0.3), 'Error');
    });
    it("return -1 from -0.7 and 0.7", function () {
	assert.equal(calculateNumber('DIVIDE', -0.7, 0.7), -1);
    });
    it("return 1 from -0.8 and -0.7", function () {
	assert.equal(calculateNumber('DIVIDE', -0.8, -0.7), 1);
    });

});
