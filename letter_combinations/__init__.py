class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        combs = []
        # for each digit
        for digit in digits:
            tmp = combs.copy()
            # for each letter for that digit
            for letter in self.getLetters(digit):
                # append letter to each existing combination
                for i in range(len(tmp)):
                    combs.append(tmp[i] + letter)
                # append letter by itself
                combs.append(letter)
        # remove combinations that arent long enough
        i = 0
        while i < len(combs):
            if len(combs[i]) != len(digits):
                combs.remove(combs[i])
            else:
                i += 1
        return combs

    def getLetters(self, digit: str):
        if digit == "2":
            return ["a", "b", "c"]
        elif digit == "3":
            return ["d", "e", "f"]
        elif digit == "4":
            return ["g", "h", "i"]
        elif digit == "5":
            return ["j", "k", "l"]
        elif digit == "6":
            return ["m", "n", "o"]
        elif digit == "7":
            return ["p", "q", "r", "s"]
        elif digit == "8":
            return ["t", "u", "v"]
        else:
            return ["w", "x", "y", "z"]
