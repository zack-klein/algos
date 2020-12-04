/**
 * Initialize your data structure here.
 * @param {number} size
 */
var empty = []

var MovingAverage = function(size) {
    this.size = size;
    this.q = [];
};

MovingAverage.prototype.avg = function(){
    let average = (array) => array.reduce((a, b) => a + b) / array.length;
    return average(this.q)
}

/**
 * @param {number} val
 * @return {number}
 */
MovingAverage.prototype.next = function(val) {
    if (this.q.length === this.size) {
        this.q.shift()
    }
    this.q.push(val)
    return this.avg()
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */
