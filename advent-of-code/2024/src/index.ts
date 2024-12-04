import fs from 'fs';

const day1data = fs.readFileSync('./src/assets/day1-data.txt', 'utf-8');
const leftNumbers: number[] = [];
const rightNumbers: number[] = [];

day1data.split('\n').forEach((line: string) => {
	const [left, right] = line.trim().split(/\s+/).map(Number);
	if (!isNaN(left) && !isNaN(right)) {
		leftNumbers.push(left);
		rightNumbers.push(right);
	}
});
leftNumbers.sort((a, b) => a - b);
rightNumbers.sort((a, b) => a - b);
let i = 0;
let res = 0;

while (i < leftNumbers.length) {
	res += Math.abs(leftNumbers[i] - rightNumbers[i]);
	i++;
}

console.log(res);
