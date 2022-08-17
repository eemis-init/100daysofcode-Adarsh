#add two numbers

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            
            #new digit
            value=v1+v2+carry
            carry=value//10
            value=value%10
            curr.next=ListNode(value)
            
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            
        return dummy.next
      
#3Sum



#longest substring repeated

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=set()
        l=0
        r=0
        for i in range(len(s)):
            while s[i] in longest:
                longest.remove(s[l])
                l+=1
            longest.add(s[i])
            r=max(r,i-l+1)
        return r
