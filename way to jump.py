
# a frog can only hop one step, or jump two steps, print out all combinations that a frog can take to reach n steps

def way_to_jump(n, path, res):
    
    if n==0:
        res.append(path)
    
    elif n==1:
        new_path = path.copy()
        new_path.append('hop')
        res.append(new_path)
        
    elif n>1:
        # one step hop
        new_path1 = path.copy()
        new_path1.append('hop')
        way_to_jump(n-1, new_path1, res)
        
        # two step jump
        new_path2 = path.copy()
        new_path2.append('jump')
        way_to_jump(n-2, new_path2, res)
        
    return res

def way_to_jump2(n):
    c0 = []
    c1 = ['hop']
    c2 = [['hop','hop'],['jump']]
    res = []
    res.append(c0)
    res.append(c1)
    res.append(c2)
    
    for i in range(3,n+1):

        # get the n-2 step and add one 'jump'
        n_2 = copy.deepcopy(res[i-2])

        if len(n_2) < 2:
            n_2.append('jump')
            n_2 = [n_2] # make it list of list
        else:
            for c in n_2:
                c.append('jump')
        
        # get the n-2 step and add one 'hop'   
        n_1 = copy.deepcopy(res[i-1])

        for c in n_1:
            c.append('hop')
    
        # combine the list together
        res.append(n_2 + n_1)
    return res[n]
  
