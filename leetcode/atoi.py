
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        integer_string = ""
        sign = "+"
        
        first_number_taken = False
        sign_taken = False
        
        for character in s:
            print(character)
            if character == ' ' and not first_number_taken and not sign_taken:
                continue;
            elif (character == '+' or character == '-') and not first_number_taken and not sign_taken:
                sign = character;
                sign_taken = True;
            elif character.isdigit():
                first_number_taken = True
                integer_string += character;
            elif not character.isdigit():
                break;
            else:
                break;
            
            
        result = 0
        if integer_string != '':
            result = int(integer_string)
        if sign == '-':
            result = 0 - result
            
        INT_MIN = -2147483648
        INT_MAX = 2147483647
    
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
            
        return result
        
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("   0-1"))