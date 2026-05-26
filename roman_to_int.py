def romanToInt(s):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    s = enumerate(list(s))
    print(s)
    out = 0
    for i in s:
        if 
            out += roman[i[1]]
        else:
            out
        
    
    return out

if __name__ == "__main__":
    print(romanToInt("VI"))