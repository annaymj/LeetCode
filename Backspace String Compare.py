```
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
```
class Solution:        
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []
        
        for char in s:
            if char != '#':
                s_list.append(char)
            elif len(s_list) != 0:
                s_list.pop()
        
        for char in t:
            if char != '#':
                t_list.append(char)
            elif len(t_list) != 0:
                t_list.pop()
        
        return s_list == t_list
