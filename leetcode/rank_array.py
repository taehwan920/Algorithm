class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        
        n = len(arr)
        ranks = {}
        for i in range(n):
            if not ranks.get(arr[i]):
                ranks[arr[i]] = []
            ranks[arr[i]].append(i)
        
        arr.sort()
        result = [0 for i in range(n)]
        rank = 0
        for i in range(n):
            now = arr[i]
            if ranks.get(now):
                rank += 1
                for idx in ranks[now]:
                    result[idx] = rank
                ranks[now] = []
            
        return result