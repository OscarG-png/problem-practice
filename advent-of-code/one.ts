import fs from "fs";

function CalibrateValues(): number {
  const values = fs
    .readFileSync("calibration-codes.txt")
    .toString()
    .split("\n");
  let result = 0;

  function FindFirst(data: string): string | undefined {
    for (let i = 0; i < data.length; i++) {
      if (parseInt(data[i])) {
        return data[i];
      }
    }
    return undefined;
  }

  function FindLast(data: string): string | undefined {
    for (let i = data.length; i > 0; i--) {
      if (parseInt(data[i])) {
        return data[i];
      }
    }
    return undefined;
  }

  for (const value of values) {
    const first = FindFirst(value);
    const last = FindLast(value);
    if (first && last) {
      const value = first + last;
      result += parseInt(value);
    }
  }
  return result;
}

const calibrationResult = CalibrateValues();
console.log("Calibration Result: ", calibrationResult);
