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
