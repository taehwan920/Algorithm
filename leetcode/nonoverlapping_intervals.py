class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x[0], x[1]))

        result = 0
        e = intervals.pop(0)[1]
        for int_s, int_e in intervals:
            if e <= int_s:
                e = int_e
            else:
                result += 1

        return result
# 틀린 풀이.


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        # 정렬한다
        result = 0
        e = intervals.pop(0)[1]
        for int_s, int_e in intervals:
            if e <= int_s:
                e = int_e
            else:
                # 정렬된 것들을 가지고 그 앞의 것의 endpoint와 현재의 startpoint를 비교해서 후자가 더 작으면 제거 카운트를 하나 올린다.
                # 여기서 제거카운트를 올리는 건 후자를 제거한다는 의미.
                result += 1
                if int_e < e:
                    # 하지만 현재의 start와 end가 전부 이전 저장한 end보다 작으면 현재의것을 삭제하는게 아닌 이전 저장한 놈을 삭제하는 것으로 방향을 전환.
                    e = int_e

        return result
