class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        d = defaultdict(set)

        for i in range(n-1):
            a, b = edges[i]
            d[a].add(b)
            d[b].add(a)

        q = [x for x in d if len(d[x]) == 1]

        while len(d) > 2:
            new_q = []
            for k in q:
                v = d.pop(k)
                v = next(iter(v))
                d[v].remove(k)
                if len(d[v]) == 1:
                    new_q.append(v)
            q = new_q

        return q