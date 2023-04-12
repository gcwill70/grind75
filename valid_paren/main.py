class Solution:
    def isValid(self, s: str) -> bool:
        numParen = numCurly = numBracket = 0
        for i in range(len(s)):
            if s[i] == "(":
                numParen += 1
            if s[i] == ")":
                numParen -= 1
            if s[i] == "{":
                numCurly += 1
            if s[i] == "}":
                numCurly -= 1
            if s[i] == "[":
                numBracket += 1
            if s[i] == "]":
                numBracket -= 1
        return numParen == numCurly == numBracket == 0
