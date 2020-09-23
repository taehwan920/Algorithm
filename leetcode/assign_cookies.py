class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        # 둘 다 정렬함으로써 그리디 알고리즘이 제대로 작동할 환경을 조성. 왜냐면 서로 작은 것 부터 비교해야하므로.
        child = 0
        cookie = 0
        result = 0

        # 각 인덱스를 child와 cookie로 핸들링함.
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # 아이가 요구하는 사이즈보다 크거나 같을 경우 쿠키를 줄 수 있으니 result에 1을 더하고 두 인덱스 다 1씩 증가
                result += 1
                cookie += 1
                child += 1
            else:
                # 아이가 요구하는 사이즈에 미치지 못할 경우, 현재 아이는 다른 아이들에 비해 가장 작은 사이즈를 요구하고 있으므로 쿠키를 더 큰 사이즈를 가져와봐야하므로
                # 쿠키 인덱스를 1 늘린다.
                cookie += 1

        return result

# 그리디 문제. 투 포인터로 해결.
