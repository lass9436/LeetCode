class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        arr = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for p in people:
            arr.insert(p[1], p)
        return arr
                    
                