def MergeSort(nums):
    n=len(nums)
    if n>1:
        mid=n//2
        left=nums[:mid]
        right=nums[mid:]
        MergeSort(left)
        MergeSort(right)

        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k] = right[j]
            j+=1
            k+=1
    return nums

a=[2,6,1,4,9,3]
print(MergeSort(a))