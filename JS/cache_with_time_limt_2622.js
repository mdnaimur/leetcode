// cache_with_time_limt_2622.js

var TimeLimitedCache = function () {
    this.cache = new Map();
}

TimeLimitedCache.prototype.set = function (key, value, duration) {
    const valueInCahce = this.cache.get(key)

    if (valueInCahce) {
        clearTimeout(valueInCahce.timeout); // clear previous timeout if key exits
    }

    // st new timeout to delte the after duration
    const timeout = setTimeout(() => {
        this.cache.delete(key)
    }, duration);

    this.cache.set(key, { value, timeout }); // store the cache 

    return Boolean(valueInCahce);
}


TimeLimitedCache.prototype.get = function (key) {
    return this.cache.get(key) ? this.cache.get(key).value : -1;

}

TimeLimitedCache.prototype.count = function () {
    return this.cache.size;
};



const cache = new TimeLimitedCache();
console.log(cache.set(1, 42, 1000)); // false, key 1 is new
console.log(cache.get(1));           // 42
setTimeout(() => console.log(cache.get(1)), 1500);  // -1, key 1 has expired
console.log(cache.count());          // 1, before timeout
