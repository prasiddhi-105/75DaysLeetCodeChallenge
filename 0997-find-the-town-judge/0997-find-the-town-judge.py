class Solution:
    def findJudge(self, n, trust):
        trust_count = [0] * (n + 1)

        for a, b in trust:
            # a trusts someone, so decrease
            trust_count[a] -= 1

            # b is trusted by someone, so increase
            trust_count[b] += 1

        # Judge will have value n-1
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i

        return -1