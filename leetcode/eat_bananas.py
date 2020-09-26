class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        start = 1
        # 최소 1개의 바나나는 먹어야하니 시작점은 1
        end = max(piles)
        # 최대값의 크기를 최대값으로 잡기

        while start < end:
            # <= 기호를 사용하여 반복문을 돌리면 시간 초과가 나옴.
            mid = (start + end) // 2

            cnt = 0
            for pile in piles:
                if pile % mid:
                    cnt += 1
                cnt += pile // mid

            if cnt > H:
                # 제한 시간 내에 다 먹지 못한 경우, 초당 바나나 섭취 스피드를 더 높여야 하므로 start값을 끌어 올려준다.
                start = mid + 1
            else:
                # 제한 시간 내에 다 먹은 경우, 초당 바나나 섭취 스피드에 문제가 없으므로 반복문을 한 번 더 돌아본다.
                end = mid

        return start
