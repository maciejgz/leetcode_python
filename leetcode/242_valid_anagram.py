class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = list(s) 
        t_array = list(t)
        
        s_array.sort()
        t_array.sort()
        
        return s_array == t_array

    
if __name__ == "__main__":
    sol = Solution();
    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagram("rat", "car"))