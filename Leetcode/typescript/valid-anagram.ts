function isValid(s: string): boolean {
  const charMap = {
    ")": "(",
    "]": "[",
    "}": "{",
  };
  let stack: string[] = [];

  for (const char of s) {
    if (char in charMap) {
      const curr = stack.length === 0 ? "!" : stack.pop();
      if (charMap[char] !== curr) {
        return false;
      }
    } else {
      stack.push(char);
    }
  }
  return stack.length === 0;
}
