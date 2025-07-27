def Longest_Common_Prefix(strs):
    result_str=""
    strs.sort()
    first_str=strs[0]
    last_str=strs[-1]
    for i  in range(min(len(first_str),len(last_str))):
        if first_str[i]!=last_str[i]:
            return result_str
        result_str+=first_str[i]
    return result_str
print(Longest_Common_Prefix(["flower","flow","flight"]))