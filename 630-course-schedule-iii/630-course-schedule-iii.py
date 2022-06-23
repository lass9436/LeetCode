from heapq import heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x : (x[1], x[0]))
        time = 0
        heap = []
        count = 0
        for course in courses:
            t, d = course
            heappush(heap, (-t, -d))
            if time + t > d:
                pt, pd = heappop(heap)
                if -pt > t:
                    time -= (-pt - t)
                else:
                    heappush(heap, (-pt, -pd))
            else:
                time += t
                count += 1
        return count
            