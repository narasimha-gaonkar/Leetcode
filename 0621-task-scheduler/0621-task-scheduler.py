class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_counter = Counter(tasks)
        res = []
        
        value_max = max(tasks_counter.values())
        
        no_max_ele = len(list(filter(lambda x: tasks_counter[x] == value_max, tasks_counter)))
        
        res = (n + 1) * (value_max - 1) + no_max_ele
        return max(res, len(tasks))