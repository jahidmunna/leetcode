import re 

class Solution:
    def myAtoi(self, s: str) -> int:
        
        lower_limit = -2147483648
        upper_limit = 2147483647
        
        #1 Read in and ignore any leading whitespace.
        s = s.lstrip()
        if not s: return 0
        
        #2 Check if the next character (if not already at the end of the string) is '-' or '+'. 
        # Read this   character in if it is either. This determines if the final result is negative or positive respectively. 
        # Assume the result is positive if neither is present.
        sign = 1
        if s[0] in ('+', '-'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
            if not s or s[0] in ('+', '-'): return 0
            
        words_in_starts = re.findall("^[A-Za-z ]+", s)
        words_in_starts = list(filter(lambda x: x !='', words_in_starts))
        if words_in_starts: return 0
        
        #3 Read in next the characters until the next non-digit character or the end of the input is reached. 
        # The rest of the string is ignored.
        digit_matched = re.findall("(\d*\.?\d*)", s)
        result = list(filter(lambda x: x !='', digit_matched))[0]
        del digit_matched
        if result:
            #4 Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
            # If no digits were read, then the integer is 0. 
            # Change the sign as necessary (from step 2).
            result = float(result) * sign
            result = int(result)
            
            #5 If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
            if result<=lower_limit:
                return lower_limit
            if result >=upper_limit:
                #6 Return the integer as the final result.
                return upper_limit
            return int(result)
        return 0


obj = Solution()
result = obj.myAtoi(s='-4193 with words')
print(result)