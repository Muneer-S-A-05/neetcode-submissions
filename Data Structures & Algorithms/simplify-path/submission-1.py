class Solution:
    def simplifyPath(self, path: str) -> str:
        array = []
        for x in path.split('/'):
            if x in ["","."]:
                continue
            if x == "..":
                if array:
                    array.pop()
            else:
                array.append(x)


        return '/' + '/'.join(array)
            