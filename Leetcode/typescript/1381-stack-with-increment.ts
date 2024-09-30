class CustomStack {
  private stack: number[];
  private maxSize: number;

  constructor(maxSize: number) {
    this.stack = [];
    this.maxSize = maxSize;
  }

  push(x: number): void {
    if (this.stack.length < this.maxSize) {
      this.stack.push(x);
    }
  }

  pop(): number {
    if (this.stack.length > 0) {
      return this.stack.pop() as number;
    } else {
      return -1;
    }
  }

  increment(k: number, val: number): void {
    for (let i = 0; i < Math.min(k, this.stack.length); i++) {
      this.stack[i] += val;
    }
  }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */
