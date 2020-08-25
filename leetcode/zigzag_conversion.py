class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            even = s[0:len(s):2]
            odd = s[1:len(s):2]
            return even + odd

        result = ''
        lines = len(s) // numRows + 1
        # 세로 줄 개수를 그냥 1을 더해서 넉넉하게 주고, 반복문 안에서는 s의 길이보다 크면 break하는 걸로 인덱스 에러를 피함으로써 혹여 라인을 부족하게 설정해 답이 틀리는 일이 없도록함
        for i in range(numRows):
            for j in range(lines):
                temp_idx = numRows * j + (numRows - 2) * j + i
                if temp_idx >= len(s):
                    break

                result += s[temp_idx]

                gap_idx = 0
                if i != 0 and i != numRows - 1:
                    gap_idx = numRows * (j+1) + (numRows - 2) * (j+1) - i
                    if gap_idx >= len(s):
                        break
                    result += s[gap_idx]
        return result
