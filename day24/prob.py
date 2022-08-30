class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r= 0,1
        distinct=set()
        maxi=0
        for i in range(len(s)):
            if s[i]==" ":
                return 0
            while s[i] in distinct:
                maxi=max(maxi,len(distinct))
                distinct.remove(s[l])
                l+=1
            distinct.add(s[i])
            r+=1
        return maxi

lol=Solution()
print(lol.lengthOfLongestSubstring(" "))