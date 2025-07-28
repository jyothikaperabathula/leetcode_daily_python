def Two_Sum(lst,target):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target:
                return i,j
print(Two_Sum([2, 7, 11, 15], 9))