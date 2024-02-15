class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        stack = []

        for i, char in enumerate(s):
            if char.lower() in vowels:
                stack.append(char)

        result = ""
        for char in s:
            if char.lower() in vowels:
                newVowel = stack.pop()
                result += newVowel
            else:
                result += char
        return result
