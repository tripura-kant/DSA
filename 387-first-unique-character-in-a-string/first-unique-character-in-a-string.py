class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = {}
        for char in s:
            if char in result:
                result[char] += 1
            else:
                result[char] = 1

        for key,value in enumerate(s):
            if result[value] == 1:
                return key
 
        return -1