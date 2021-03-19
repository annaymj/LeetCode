# Given a string, find the length of the longest substring without repeating characters.
# e.g. Given 'abcabcbb', the answer is 'abc', with the length of 3
# e.g. 'bbbbb', the answer is 'b', with the length of 1
# e.g. 'pwwkew', the answer is 'wke', the length is 3 
def longestUniqueSubsttr(input_str):
    last_idx = {} # last index of every character
    max_len = 0
    start = 0
    # starting index of current window to calculate max_len
    start_idx = 0

    for i in range(0, len(input_str)):
    # Find the last index of str[i], update start_idx (starting index of current window) as maximum of current value of start_idx and last index plus 1
        if input_str[i] in last_idx:
            start_idx = max(start_idx, last_idx[input_str[i]] +1)

        # Update result if we get a larger window
            new_len = i-start_idx + 1
            if new_len > max_len:
                max_len = new_len
                start  = start_idx
                   
                   
        # Update last index of current char.
        last_idx[input_str[i]] = i

    return (max_len, input_str[start:start+max_len])

