const x = 2;
let y = 4;

function update(arg) {
  return Math.random() + y * arg;
}

y = 3; // Adjusted value to ensure the result is between 6 and 7

const result = update(x);

console.log(result);
