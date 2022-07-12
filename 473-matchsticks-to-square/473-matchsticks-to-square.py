class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot = sum(matchsticks)
        if tot % 4 != 0:
            return False
        for n in matchsticks:
            if n > tot / 4:
                return False
        m = tot / 4
        hm = {}
        matchsticks.sort()
        def helper(side, length, used):
            if used in hm:
                return hm[used]
            if side == 4 and length == 0:
                hm[used] = True
                return True
            for i in range(len(matchsticks)):
                if matchsticks[i] + length > m:
                    break
                if not (used >> i & 1):
                    used = used | (1 << i)
                    ret = False
                    if matchsticks[i] + length < m:
                        ret = helper(side, matchsticks[i] + length, used)
                    else:
                        ret = helper(side + 1, 0, used)
                    used = used ^ (1 << i)
                    if ret:
                        hm[used] = True
                        return True
            hm[used] = False
            return False
        return helper(0, 0, 0)