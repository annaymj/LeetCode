```
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```


from collections import defaultdict

class Solution:
    # postorder DFS: 
    # rationale: if the subgraph formed by all descendant nodes from this node has no cycle, 
    # then adding this node to the subgraph would not form a cycle either.
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = defaultdict(list)
       
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)
        
        checked = [False] * numCourses
        path = [False] * numCourses
        
        for currCourse in range(numCourses):
            if self.isCycle(currCourse, courseDict, path, checked):
                return False
        return True
    
    def isCycle(self, currCourse, courseDict, path, checked):
        if checked[currCourse] == True: # if the node has been checked, no cycle would be formed with this node
            return False 
        
        if path[currCourse] == True: # marked a node has cycle in the path
            return True
        
        path[currCourse] = True # mark the node in the path
        
        ret = False
        
        for child in courseDict[currCourse]: # postorder DFS, visit all its children first
            ret = self.isCycle(child, courseDict,path,checked)
            if ret == True:
                break
                
        path[currCourse] = False  # after backtracking, remove the node from the path
        checked[currCourse] = True # make this node as checked
        return ret
        
