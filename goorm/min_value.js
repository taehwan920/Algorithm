// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = [];

const solution = arr => {
    let n = Number(arr[0]);
    let nums = arr[1].split(' ').map(item => Number(item));
    nums.sort((a, b) => a - b);
    return nums[0];
};

let count = 0
rl.on("line", function (line) {
    input.push(line)
    count++
    if (count === 2) { rl.close() };
}).on("close", function () {
    console.log(solution(input));
    process.exit();
});