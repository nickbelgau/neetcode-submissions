class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
        for count in char_count.values():
            if count != 0:
                return False
        return True