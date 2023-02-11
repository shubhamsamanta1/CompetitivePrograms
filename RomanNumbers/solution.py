def romanToInt(s):
    Closet = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    total = 0
    for i in range (len(s)):
        if i > 0 and Closet.get(s[i]) > Closet.get(s[i-1]):
            total += Closet.get(s[i]) - 2*Closet.get(s[i-1])
        else:
            total += Closet.get(s[i])
    return total


s = "XXCD"
print(romanToInt(s)) 