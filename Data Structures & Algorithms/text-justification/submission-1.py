class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line,length = [],0
        i = 0
        while i < len(words):
            # if line complete
            if length + len(line) + len(words[i]) > maxWidth:
                totalspaces = maxWidth - length

                # if single word
                if len(line) == 1:
                    res.append(line[0]+(' ' * totalspaces))
                    line,length = [],0
                    continue

                spaces = totalspaces // max(len(line)-1,1)
                additional = totalspaces % max(len(line)-1,1)

                for j in range(len(line)-1):
                    line[j] += ' ' * spaces
                    if additional:
                        line[j] += ' '
                        additional -= 1
                
                res.append(''.join(line))
                line,length = [],0
                continue
            
            # if line has space left
            line.append(words[i])
            length += len(words[i])
            i += 1

        # last line
        lastline = ' '.join(line)
        totalspaces = maxWidth - len(lastline)
        res.append(lastline + ' ' * totalspaces)

        return res