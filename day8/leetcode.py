#reverse bits (wrong)
class Solution:
    def reverseBits(self, n: int) -> int:
        A=str(n)
        A=A[-1::]
        m=len(A)
        A=int(A)
        sum=0
        for i in range(m):
            sum+=A>>1
            A=A>>1
        print(sum)
