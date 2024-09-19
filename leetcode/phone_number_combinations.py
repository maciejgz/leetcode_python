from typing import List



class Solution:
    
    def __init__(self):
        self.digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        listtt = self.findPossibilities(digits)
        return listtt
    
    def findPossibilities(self, sufix: str) -> List[str]:
        if len(sufix) == 1:
            return list(self.digit_to_letters[sufix])    
        
        result = []
        for letter in self.digit_to_letters[sufix[0]]:
            new_suffix = sufix[1:]
            sufix_array = self.findPossibilities(new_suffix);
            for possibility in sufix_array:
                result.append(letter + possibility)
                
        return result
        
    
        
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("322"))