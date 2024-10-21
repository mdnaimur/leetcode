// compact_object_2705.js


var compactObject = function (obj) {

    if (Array.isArray(obj)) {
        return obj.map(compactObject).filter(Boolean);
    }

    else if (typeof obj === 'object' && obj !== null) {
        return Object.keys(obj).reduce((acc, key) => {
            const value = compactObject(obj[key]);
            if (Boolean(value)) {
                acc[key] = value;
            }
            return acc;
        }, {})
    }

    return obj
};

// Example Usage
const obj = {
    a: null,
    b: [false, 1, "", "hello"],
    c: {
        d: 0,
        e: undefined,
        f: "world",
        g: [null, 2, 3]
    },
    h: 0
};

const compacted = compactObject(obj);
console.log(compacted);