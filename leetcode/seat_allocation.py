def judge(a, b, c, d):
    if a and b and c and d:
        return 2
    if a and b:
        return 1
    if c and d:
        return 1
    if b and c:
        return 1
    return 0


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        r = sorted(reservedSeats, key=lambda x: (x[0], x[1]))
        seats = {}
        for row, seat in r:
            if not seats.get(row):
                seats[row] = []
            seats[row].append(seat)

        result = 0
        count = 0
        side_l = [2, 3]
        side_r = [8, 9]
        center_l = [4, 5]
        center_r = [6, 7]
        for booked in seats:
            count += 1
            l = c_l = c_r = r = True
            for seat in seats[booked]:
                if seat in side_l:
                    l = False
                if seat in side_r:
                    r = False
                if seat in center_l:
                    c_l = False
                if seat in center_r:
                    c_r = False
            result += judge(l, c_l, c_r, r)

        result += 2 * (n - count)
        return result
