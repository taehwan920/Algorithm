class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        moved = 0
        # 몇 번 이동 했는지 체크
        visited = 0
        # 실제로 가스를 이동한 횟수
        idx = 0

        tank = -1
        start = -1
        while visited < n and moved < 2 * n + 1:
            # visited는 tank가 양수로 유지될 때에만 증가하며, 음수로 내려가게되면 0으로 초기화되는 변수
            # moved는 각 station을 체크한 횟수.
            # 현재 접근 방법은 station을 index 0 부터 하나하나씩 방문하며 해당 station이 start지점이 될 자격이 있는가 검사해야하므로 각 주유소를 최소 한 번씩 돌아야함
            # 한 번 도는 중간에 start가 될만한 지점이 있으면 일단 한 번 또 추가로 돌아야하기 때문에 moved가 2n+1보다 커지면 두 번 돌았는 데도 gas가 충분해지는 start지점을 찾지 못했다는 뜻이므로 반복문 종료.
            prev_i = idx - 1 if idx - 1 >= 0 else n - 1
            # 이전 idx
            tank -= cost[prev_i]
            # 가스 소모량을 탱크에서 빼줌
            if tank < 0:
                tank = gas[idx]
                visited = 0
                start = idx
                # 이전 주유소에서 채운 기름으로 도착할 수 없었던 곳이었다면 현재 지점을 스타트 지점으로 삼고 다시 시작
            else:
                tank += gas[idx]
                visited += 1
                # 만약 기름이 남아있다면 갈 수 있단 소리니 기름도 채우고 visited도 1증가.

            moved += 1
            idx = idx + 1 if idx + 1 < n else 0

        # 만약 조건에 맞는 출발점 주유소를 moved가 2n + 1이 되도록 발견하지 못했다면 -1, 아니라면 start 포인트의 인덱스를 반환
        return start if moved != 2 * n + 1 else -1
