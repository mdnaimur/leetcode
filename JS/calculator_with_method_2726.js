// calculator_with_method_2726.js


class Calculator {

    /** 
     * @param {number} value
     */
    constructor(value) {
        this.x = value;
    }

    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value) {
        this.x += value;
        return this
    }

    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value) {
        this.x -= value;
        return this
    }

    /** 
     * @param {number} value
     * @return {Calculator}
     */
    multiply(value) {
        this.x *= value;
        return this
    }

    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if (value === 0) {
            throw new Error("Division by zero is not allowed");
        }
        this.x /= value;
        return this
    }

    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        this.x = Math.pow(this.x, value);
        return this
    }

    /** 
     * @return {number}
     */
    getResult() {
        return this.x;
    }
}

//example 
const calculator = new Calculator(10);

// Perform chained operations
const result = calculator
    .add(5)           // 10 + 5 = 15
    .subtract(3)      // 15 - 3 = 12
    .multiply(2)      // 12 * 2 = 24
    .divide(4)        // 24 / 4 = 6
    .power(3)         // 6^3 = 216
    .getResult();     // Get the final result

console.log(result); // Output: 216
