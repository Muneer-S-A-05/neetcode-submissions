class Solution:
    def simplifyPath(self, path: str) -> str:
        array = []
        temp = ''
        for x in path:
            if not temp and x=='/':
                continue
            if temp and x=='/':
                if temp=='..':
                    if array:
                        array.pop()
                elif temp!='.':
                    array.append(temp)
                temp = ''
            else:
                temp += x

        if temp:
            if temp=='..':
                if len(array)>1:
                    array.pop()
            elif temp!='.':
                array.append(temp)

        return '/' + '/'.join(array)
            