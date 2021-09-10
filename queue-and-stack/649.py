class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ban = [False] * len(senate)
        rad = sum([ch == 'R' for ch in senate])
        ban_rad = 0
        dire = sum([ch == 'D' for ch in senate])
        ban_dire = 0
        while rad > 0 and dire > 0:
            for i, ch in enumerate(senate):
                if ban[i]:
                    continue
                if ch == 'R' and ban_rad == 0:
                    ban_dire += 1
                elif ch == 'D' and ban_dire == 0:
                    ban_rad += 1
                elif ch == 'R' and ban_rad > 0:
                    ban[i] = True
                    ban_rad -= 1
                    rad -= 1
                elif ch == 'D' and ban_dire > 0:
                    ban[i] = True
                    ban_dire -= 1
                    dire -= 1
        if rad > 0:
            return 'Radiant'
        else:
            return 'Dire'

if __name__ == '__main__':
    sol = Solution()
    senates = ['RD', 'RDD', 'RRDDD', 'DDRR']
    for senate in senates:
        print(sol.predictPartyVictory(senate))

