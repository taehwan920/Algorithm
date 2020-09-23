class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0  # 로봇 위치
        dx, dy = 0, 1  # 이동 방향
        obs = {tuple(i) for i in obstacles}  # 빠른 접근을 위한 set 자료형 활용
        maxdist = 0  # 가장 멀리 간 거리 저장

        for step in commands:
            if 0 < step < 10:
                for i in range(step):
                    x, y = x+dx, y+dy   # step에 나온 좌표를 향해 1씩 전진
                    if (x, y) in obs:   # 전진한 좌표가 장애물 좌표에 해당한다면 바로 그 전 좌표에서 멈춤
                        x, y = x-dx, y-dy
                        break
            # 좌회전 : dy와 dx의 자리를 바꾸고, 마이너스 기호를 붙여줌으로써 간단하게 구현할 수 있음.
            elif step == -2:
                dx, dy = -dy, dx
            elif step == -1:  # 우회전도 마찬가지
                dx, dy = dy, -dx

            maxdist = max(maxdist, x**2 + y**2)

        return maxdist
