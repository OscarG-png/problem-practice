function isPalindrome(s: string): boolean {
    let l = 0;
    let r = s.length - 1;

    while (l < r) {
        while (l < r && !isAlNum(s[l])) {
            l++;
        }
        while (l < r && !isAlNum(s[r])) {
            r--;
        }
        if (s[l].toLowerCase() !== s[r].toLowerCase()) {
            return false;
        }
        l++;
        r--;
    }

    return true;
}
function isAlNum(char: string): boolean {
    return char.length === 1 && char.match(/[a-z0-9]/i) !== null;
}
