class Solution:
    def removeDuplicates(self, S: str) -> str:
        delete = True

        while delete:
            delete = False

            S = list(S)

            idx = 0
            while idx < len(S) - 1:
                if S[idx] == S[idx + 1]:
                    S.pop(idx)
                    S.pop(idx)
                    delete = True
                else:
                    idx += 1

        return ''.join(S)
