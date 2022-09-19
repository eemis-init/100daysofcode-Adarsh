class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[0 for _ in range(i)] for i in range(1, numRows + 1)]
        for i in range(numRows):
            for j in range(i+1):
                if j==0 or j==len(result[i])-1:
                    result[i][j]=1
                else:
                    result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result
