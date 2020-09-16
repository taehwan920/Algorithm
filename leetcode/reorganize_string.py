class Solution:
    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        # 주어진 문자열에 나오는 알파벳이 나온 갯수와 해당 알파벳을 묶어서 최대 힙에 저장
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""
        # 각 알파벳을 돌면서 해당 알파벳 개수가 전체문자열 길이+1 의 반이 넘을 경우 서로 같은 글자가 붙는 상황이 나오게 되어 빈 문자열 리턴

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            # 최대 힙을 이용해 아직 개수가 많이 남은 글자부터 꺼내서 ans에 붙임
            # 두개씩 하는 이유는 한개씩만 하면 같은 글자가 붙게 될 수 있기 때문
            ans.extend([ch1, ch2])
            if nct1 + 1:
                heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1:
                heapq.heappush(pq, (nct2 + 1, ch2))
            # 이번 nct값이 1이었다면 해당 알파벳의 마지막 글자까지 다 쓴 것이 되므로 더이상 힙에 넣지 않는다.

        return "".join(ans) + (pq[0][1] if pq else '')
        # 아직 힙에 엘리먼트가 하나 남아있다면 그걸 마저 넣어주고 아닐 경우 빈 문자열만 더해준다.
