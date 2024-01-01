function kangaroo(x1, v1, x2, v2) {
    if (v1 !== v2 && (x2 - x1) % (v1 - v2) === 0 && (x1 - x2) / (v2 - v1) >= 0) {
        return "YES";
    }
    return "NO";
}

/* this problem was about finding if two kangaroos at position x1 and x2 will eventually jump to the same position,
their jumping distance is v1 and v2 respectively. I had to find if they will ever meet at the same position.
*/
