"""Class object to convert roman numerals
to integers. I kept raising errors, since
I am solving this problem on my local machine
and practising everything I can.
"""

class Solution: 
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        rng = range(1, 4000)

        if len(s) > 15:
            raise ValueError("Roman numeral shouldn't be larger than 15")
        
        for num in s:
            if num not in roman:
                raise ValueError("Input must be valid roman numerals")

        out = 0
        previous = 0

        for i in reversed(s):

            if roman[i] >= previous:
                out += roman[i]
            else:
                out -= roman[i]
            
            second_previous = previous
            previous = roman[i]

        if out not in rng:
            raise ValueError("Input must be in range [1, 3999]")
        return out
    
if __name__ == "__main__":
    s = input("Roman numerals:\n")
    solution = Solution()
    print(solution.romanToInt(s))
