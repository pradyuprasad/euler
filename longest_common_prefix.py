def longest(L):
    if "" in L:
        return ""
    else:
        end = len(min(L, key=len))
        prefix = ""
        for i in range(0, end):
            current = L[0][i]
            all_equal = True
            for j in range(1, len(L)):
                if L[j][i] != current:
                    all_equal = False
                    break
                
            if not all_equal:
                return prefix
            else:
                prefix += current
        
        return prefix


strs = ["flower","flow","flight"]

print(longest(strs))