#Twosum 2

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
                
#roman to integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        for i in range(len(s)):
            if i+1 < len(s) and roman_val[s[i]]<roman_val[s[i+1]]:
                res-=roman_val[s[i]]
            else:
                res+=roman_val[s[i]]
        return res
            
#integer to roman

class Solution:
    def intToRoman(self, num: int) -> str:
        res=''
        roman = [['I',1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],['L',50],['XC',90],['C',100],['CD',400],['D',500],['CM',900],['M',1000]]
        for sym, val in reversed(roman):
            if num//val:
                copy = num//val
                res+=copy*sym
                num=num%val
        return res
            
#most common word

#bruteforce (TLE)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                spill = min(height[i],height[j])
                area=spill*(j-i)
                maxVol =  max(maxVol, area)
        return maxVol
    
#two pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol=0
        l, r = 0, len(height)-1
        
        while l<r:
            area = (r-l)*min(height[r],height[l])
            maxVol=max(area,maxVol)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxVol
    
    #rotate image
    
    class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r =0,len(matrix)-1
        while l<r:
            for i in range(r-l):
                top,bottom=l,r
                topleft=matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topleft
            
            l+=1
            r-=1
        return matrix
                
        #valid parenthesis
        
        class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairing = {')':'(',']':'[','}':'{'}
        
        for i in s:
            if i in pairing:        
                if stack and stack[-1]==pairing[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if stack==[] else False
