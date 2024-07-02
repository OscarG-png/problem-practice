import fs from "fs";

function CalibrateValues(): number {
  const values = fs.readFileSync("calibration-codes.txt", "utf-8").split("\n");
  let result = 0;

  function FindFirst(data: string): string | undefined {
    for (let i = 0; i < data.length; i++) {
      const num = parseInt(data[i]);
      if (!isNaN(num)) {
        return data[i];
      }
    }
    return undefined;
  }

  function FindLast(data: string): string | undefined {
    for (let i = data.length; i > 0; i--) {
      const num = parseInt(data[i]);
      if (!isNaN(num)) {
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
      console.log("Value: ", value);
      result += parseInt(value);
      console.log("Result: ", result);
    }
  }
  return result;
}

const calibrationResult = CalibrateValues();
console.log("Calibration Result: ", calibrationResult);
