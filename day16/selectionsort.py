def SelectionSort(nums):
    for i in range(len(nums)):
        min_position = i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min_position]:
                min_position=j
        temp=nums[i]
        nums[i]=nums[min_position]
        nums[min_position]=temp
    return nums

a=[2,6,1,4,9,3]
print(SelectionSort(a))