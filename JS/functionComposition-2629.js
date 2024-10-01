// function compose(functions) {
//   return function (x) {
//     return functions.reduceRight((acc, fn) => fn(acc), x);
//   };
// }

function compose(functions) {
  return function (x) {
    const n = functions.length
    for (let i = n - 1; i >= 0; i--) {

      x = functions[i](x);
    }
    return x;
  };
}

// Example usage
const f1 = x => x + 1;
const f2 = x => x * 2;
const f3 = x => x - 3;

const functions = [f1, f2, f3];
const composedFn = compose(functions);
const result = composedFn(5);  // Equivalent to f1(f2(f3(5))) -> f1(f2(2)) -> f1(4) -> 5
console.log(result);  // Output: 5
