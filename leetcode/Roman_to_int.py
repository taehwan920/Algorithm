class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        def pre_is_bigger(pre, nex):
            if nums[pre] < nums[nex]:
                return False
            return True
        # 4, 9, 40, 90 등은 두 글자 중 앞에 써있는 글자가 더 작은 수 인 경우에 해당하므로 그걸 판별하는 함수를 작성

        result = 0
        jump = 0
        last_is_that = False
        for i in range(len(s)-1):
            if jump:
                jump -= 1
                continue
            if pre_is_bigger(s[i], s[i+1]):
                result += nums[s[i]]
            else:
                if i == len(s)-2:
                    last_is_that = True
                jump += 1
                result += nums[s[i+1]] - nums[s[i]]

        if not last_is_that:
            result += nums[s[len(s)-1]]
        # 위의 반복문을 돌리면 맨 마지막 숫자는 더하지 않고 끝나게 되는데, 만약 마지막 숫자가 4, 9, 40 등의 숫자에 해당한다면 마지막 숫자를 더하지 않고 끝내고, 해당하지 않으면 더해준다.
        return result
