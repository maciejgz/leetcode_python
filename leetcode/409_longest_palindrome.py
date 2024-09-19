
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if str is None or len(s) == 0:
            return 0;
        if len(s) == 1:
            return 1;
        
        characters = {}
        max_palindrome_len = 0
        for char in s:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
            
        odd_found = 0    
        for count in characters.values():
            if count % 2 == 0:
                max_palindrome_len += count
            else:
                max_palindrome_len += count - 1
                odd_found = True
                
        if odd_found:
            max_palindrome_len += 1 
                
        return max_palindrome_len

if __name__ == "__main__":
    solution = Solution()
    
    print(solution.longestPalindrome(""))
    print(solution.longestPalindrome("a"))
    print(solution.longestPalindrome("anna"))