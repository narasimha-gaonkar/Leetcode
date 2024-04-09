class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import defaultdict
        student_map = defaultdict(list)
        for i,val in enumerate(students):
            student_map[val].append(i)
        
        for i,val in enumerate(sandwiches):
            if student_map[val]:
                student_map[val].pop(0)
            else:
                return len(sandwiches) - i
        return 0