class MyCalendarTwo {
  private nonOverlapping: [number, number][];
  private overlapping: [number, number][];

  constructor() {
    this.nonOverlapping = [];
    this.overlapping = [];
  }

  book(start: number, end: number): boolean {
    for (const [s, e] of this.overlapping) {
      if (!(end <= s || e <= start)) {
        return false;
      }
    }

    for (const [s, e] of this.nonOverlapping) {
      if (end > s && e > start) {
        this.overlapping.push([Math.max(s, start), Math.min(e, end)]);
      }
    }

    this.nonOverlapping.push([start, end]);
    return true;
  }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * var obj = new MyCalendarTwo()
 * var param_1 = obj.book(start,end)
 */
