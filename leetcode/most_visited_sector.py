class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        visited = [0 for i in range(n+1)]
        visited[rounds[0]] += 1

        for i in range(1, len(rounds)):
            if rounds[i-1] > rounds[i]:
                for j in range(1, n+1):
                    if j <= rounds[i]:
                        visited[j] += 1
                    if j > rounds[i-1]:
                        visited[j] += 1
            elif rounds[i-1] == rounds[i]:
                visited[i] += 1
            elif rounds[i-1] < rounds[i]:
                for j in range(rounds[i-1] + 1, rounds[i] + 1):
                    visited[j] += 1

        most = max(visited)
        result = []
        for i in range(1, len(visited)):
            if visited[i] == most:
                result.append(i)
        return result
