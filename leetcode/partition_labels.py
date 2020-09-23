class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        # 각 알파벳 별 가장 큰 인덱스를 저장
        start, end = 0, 0
        # 투 포인터. anchor는 나눈 문자열 묶음의 가장 앞 인덱스를 가리키게 됨. j는 그 묶음의 가장 뒷 인덱스를 가리킴.

        result = []

        for i, c in enumerate(S):
            end = max(end, last[c])
            # 문자열 묶음의 가장 큰 인덱스를 선택.
            if i == end:
                # 만약 가장 큰 인덱스 까지 왔다면
                result.append(len(S[start:end+1]))
                # 그 길이를 저장. 사실 위의 것보단 len(S[anchor:j+1])를 하는게 더 가독성이 좋았을 것.
                start = i + 1
                # 바로 다음 인덱스를 문자열 묶음의 첫 인덱스로 지정.
        return result

# 그리디 문제 중 투 포인터로 풀 수 있는 문제들이 꽤 있는 듯함.
