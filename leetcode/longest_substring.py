class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print("s: ", s)
        str_len = len(s)
        if str_len == 0:
            return 0
        if str_len == 1:
            return 1    
        max_len = 0
        start = 0
        end = 0
        char_set = set()
        print("str_len: ", str_len)
        while end < str_len:
            if s[end] not in char_set:
                print('adding character: ', s[end])
                char_set.add(s[end])
                end += 1
                max_len = max(max_len, end - start)
            else:
                print('repeat: ', s[end])
                char_set.remove(s[start])
                start += 1
        return max_len
        
        
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("ssammple"))