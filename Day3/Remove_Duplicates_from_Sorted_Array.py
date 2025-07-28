def Remove_Duplicates_from_Sorted_Array(nums):
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
print(Remove_Duplicates_from_Sorted_Array([0, 0, 1, 1, 2, 2, 3]))