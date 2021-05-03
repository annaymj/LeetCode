def flattenList(nestedList):
    res = []
    
    for i in range(len(nestedList)):
        curr = nestedList[i]
        flatten_helper(curr,res)
    
    return res

def flatten_helper(curr,res):
    if type(curr) == int:
        res.append(curr)
    else:
        for i in range(len(curr)):
            flatten_helper(curr[i],res)
