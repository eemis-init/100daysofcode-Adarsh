#implement strstr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle :
                return i
        return -1
      
#group anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for i in strs:
            words[tuple(sorted(i))].append(i)
        return list(words.values())
    
   
