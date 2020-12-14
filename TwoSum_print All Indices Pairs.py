# given array = [1,3,3,5,7] return all pairs of indices where values add to K. Order doesn't matter
####################################### Version 1 ################################################
def pairsAddUpToK(array,k):
    result=set()
    num_dict = {}
    
    # step 1: store values to a dictionary, where numbers are key, indexes stored as list
    for i in range(len(array)):
        num = array[i]
        
        # if already in the key list, append index
        if num in num_dict.keys():
            num_dict[num].append(i)
        # if not there, initiatilize a list and add the number
        else:
            num_dict[num] = [i]
    
    # step2: search for pairs
    for num in num_dict.keys():
        # if pair exist and are 2 different numbers  
        if k - num in num_dict.keys() and k - num != num:
            # loop through both value lists and create all combinations
            for i in range(len(num_dict[num])):
                for j in range(len(num_dict[k-num])):
                    pair = (num_dict[num][i],num_dict[k-num][j])
                    pair_c = (num_dict[k-num][j],num_dict[num][i])
                    
                    # check whether the mirrored result in result or not
                    if pair_c not in result:
                        result.add(pair)
            
        
        # if pair exist and it is the same number
        if k - num in num_dict.keys() and k - num == num:
            if len(num_dict[num]) == 2:
                pair = (num_dict[num][0],num_dict[num][1])
                result.add(pair)
            else:
                # loop through value list and create all combinations
                index_list = num_dict[num]
                for i in range(len(index_list)-1):
                    for j in range(i+1, len(index_list)):
                        pair = (index_list[i],index_list[j])
                        result.add(pair)
              
    return result
    

####################################### Version 2 ################################################
def pairsAddUpToK2(array,k):
    result=set()
    num_dict = {}
    num_checked = {}

    # step 1: store values to a dictionary, where numbers are key, indexes stored as list
    for i in range(len(array)):
        num = array[i]
        
        # if already in the key list, append index
        if num in num_dict.keys():
            num_dict[num].append(i)
        # if not there, initiatilize a list and add the number
        else:
            num_dict[num] = [i]
    
    # step2: search for pairs
    for num in num_dict.keys():
        
        if num not in num_checked.keys():
            
            # if pair exist and are 2 different numbers 
            if k - num in num_dict.keys() and k - num != num:
                # loop through both value lists and create all combinations
                num_checked[num] = True
                num_checked[k-num] = True
                for i in range(len(num_dict[num])):
                    for j in range(len(num_dict[k-num])):
                        pair = (num_dict[num][i],num_dict[k-num][j])
                        result.add(pair)


            # if pair exist and it is the same number
            if k - num in num_dict.keys() and k - num == num:
                num_checked[num] = True
                if len(num_dict[num]) == 2:
                    pair = (num_dict[num][0],num_dict[num][1])
                    result.add(pair)
                else:
                    # loop through value list and create all combinations
                    index_list = num_dict[num]
                    for i in range(len(index_list)-1):
                        for j in range(i+1, len(index_list)):

                            pair = (index_list[i],index_list[j])
                            result.add(pair)

    return result
            
            
