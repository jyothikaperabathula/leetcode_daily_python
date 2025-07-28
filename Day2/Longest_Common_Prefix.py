def longest_common_prefix(strs):
    res="" 
    strs.sort()
    first=strs[0]
    last=strs[-1]
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return res
        res+=first[i]
    return res
print(longest_common_prefix(["flower","flow","flight"]))