class Tree {
    left: Tree | null;
    right: Tree | null;
    start: number;
    end: number;

    constructor(start: number, end: number) {
        this.left = null;
        this.right = null;
        this.start = start;
        this.end = end;
    }

    insert(start: number, end: number): boolean {
        if (end <= this.start) {
            if (this.left === null) {
                this.left = new Tree(start, end);
                return true;
            }
            return this.left.insert(start, end);
        } else if (start >= this.end) {
            if (this.right === null) {
                this.right = new Tree(start, end);
                return true;
            }
            return this.right.insert(start, end);
        } else {
            return false; // Overlap detected
        }
    }
}
class MyCalendar {
    root: Tree | null;

    constructor() {
        this.root = null;
    }

    book(start: number, end: number): boolean {
        if (!this.root) {
            this.root = new Tree(start, end);
            return true;
        }
        return this.root.insert(start, end);
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */
