class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0
        total = 0
        q = [id]
        while q:
            now = q.pop(0)
            now_e = None
            for e in employees:
                if e.id == now:
                    now_e = e
            total += now_e.importance
            for sub_e in now_e.subordinates:
                q.append(sub_e)

        return total
