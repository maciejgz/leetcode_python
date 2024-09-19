class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ## stworzyć mapę z magazine
        char_count = {}
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        ## iterować po znakach w ransom note i odejmować znaki z hashmapy utworzonej z magazine
        for char in ransomNote:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                return False
        return True
        