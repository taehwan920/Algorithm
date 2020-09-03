class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = ''
        for i in range(len(paths)):
            dest = paths[i][1]
            for j in range(len(paths)):
                if paths[i][1] == paths[j][0]:
                    break
            else:
                return dest
