class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return -1
        if len(trust) == 1:
            return trust[0][1]

        adjaceny_list = defaultdict(list)

        for people in trust:
            adjaceny_list[people[0]].append(people[1])
        
        town_judge = 0
        for i in range(1, n+1):
            if i in adjaceny_list:
                continue
            else:
                town_judge = i

        count = 0
        for key,value in adjaceny_list.items():
            if key != town_judge and town_judge in value:
                count += 1
        
        if count == (n-1):
            return town_judge
        else:
            return -1

                
