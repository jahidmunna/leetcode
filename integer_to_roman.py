# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

 

# Example 1:
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.

# Example 2:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1 : 'I',
            5 : 'V',
            10 : 'X',
            50 : 'L',
            100 : 'C',
            500 : 'D',
            1000 : 'M'
        }
        
        roman = ""
        
        while num: 
            if num>=1000:
                roman += mapping[1000]
                num -= 1000
            elif num>=500:
                roman += mapping[500]
                num -= 500
            elif num>= 100:
                roman += mapping[100]
                num -= 100
            elif num>=50:
                roman += mapping[50]
                num -= 50
            elif num>=10:
                roman += mapping[10]
                num -= 10
            elif num>=5:
                roman += mapping[5]
                num -= 5
            else:
                roman += mapping[1]
                num -=1
        
        if roman:
            roman = roman.replace("IIII", "IV").replace("VIV", "IX")
            roman = roman.replace("XXXX", "XL").replace("LXL", "XC")
            roman = roman.replace("CCCC", "CD").replace("DCD", "CM")
            
        return roman
    
obj = Solution()
result = obj.intToRoman(1994) #"MCMXCIV"
result = obj.intToRoman(58) #"LVIII"

print(result)