class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):  # 여기는 첫 글자 인덱스 선정
            # 여기서 마지막 글자 인덱스 선정, 가장 긴 것 부터 차례대로 체크..
            for j in range(len(s), i, -1):
                if len(result) >= j - i:  # result에 저장된 값보다 짧으면 무시
                    break
                elif s[i:j] == s[i:j][::-1]:  # 회문 체크
                    result = s[i:j]
                    break
        return result
