# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
# you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
            
        # Make graph and Degree first
        graph = defaultdict(list)
        degree = {}
        # given_couses = set()
        for course, prerequisite in prerequisites:
            # given_couses.add(course)
            # given_couses.add(prerequisite)
            graph[prerequisite].append(course)
            degree[course] = degree.get(course, 0)+1
        
        # Get Zero Degree Couses 
        zero_degress = deque(i for i in range(numCourses) if i not in degree)
        # print(zero_degress)
        total_courses = []
        while zero_degress:
            prerequisit = zero_degress.popleft()
            total_courses.append(prerequisit)
            courses = graph[prerequisit]
            for course in courses:
                degree[course] -=1
                
                if degree[course] == 0:
                    zero_degress.append(course)
        
        # print(total_courses)
        # return len(total_courses) == len(given_couses)
        return len(total_courses) == numCourses


obj = Solution()
# result = obj.canFinish(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
result = obj.canFinish(numCourses = 5, prerequisites = [[1,4],[2,4],[3,1],[3,2]])

print(result)