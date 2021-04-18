```
A string can be abbreviated by replacing any number of non-adjacent substrings with their lengths. For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
Note that "s55n" ("s ubsti tutio n") is not a valid abbreviation of "substitution" because the replaced substrings are adjacent.

Given a string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
 

Constraints:

1 <= word.length, abbr.length <= 20
word consists of only lowercase English letters.
abbr consists of lowercase English letters and digits.
```
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:        
        i = 0 #index for abbr
        j = 0 #index for word
        while i < len(abbr): 
            # if out of range, return False
            if j >= len(word):
                return False
            
            if abbr[i].isnumeric() == False:
                if abbr[i] != word[j]:
                    return False
                else: # if the chars equal
                    i += 1
                    j += 1
                    
            # if the next char is not numeric
            elif abbr[i].isnumeric() == True and i+1 < len(abbr) and abbr[i+1].isnumeric() == False:
                if abbr[i] == '0':
                    return False
                else:   
                    j += int(abbr[i]) 
                    i += 1
                
            # if the next char is also numeric, max 2 digits
            elif abbr[i].isnumeric() == True and i+1 < len(abbr) and abbr[i+1].isnumeric() == True:
                if abbr[i] == '0':
                    return False
                else:
                    j += int(abbr[i:i+2])
                    i += 2
      
            # if this numeric char is the last digit
            elif abbr[i].isnumeric() == True and i == len(abbr) - 1:
                j += int(abbr[i])
                i += 1
    
        return j == len(word)
                
