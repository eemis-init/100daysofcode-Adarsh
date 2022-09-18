
numRows = 3
result = [[1]]
for i in range(1,numRows):
    if i == 1:
        result.append([1,1])
    else:
        end = len(result[i-1])+1
        for j in range(end):
            # if j == 0 or j == end-1:
            #     result[i][j].append(1)
            #     print(result)
            # else:
            result[i][j].append(result[i-1][j] + result[i-1][j+1])
            print(result)
                                    
print(result)
