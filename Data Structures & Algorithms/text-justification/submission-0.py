class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        def justified(s,l):
            combined = s[0]
            spaces = maxWidth - l
            additional = spaces % (len(s)-1 if len(s)>2 else 1)
            for x in s[1:]:
                fac = (spaces//(len(s)-1)) + (1 if additional else 0)
                combined += ' ' * fac + x
                if additional: additional -= 1
            return combined

        i = 0
        while i < len(words):
            length = len(words[i])
            s = [words[i]]
            while i+1 < len(words) and length+len(words[i+1])+len(s)-1 < maxWidth:
                s.append(words[i+1])
                length += len(words[i+1])
                i += 1
            if i+1<len(words) and len(s)>1:
                res.append(justified(s,length))
            else:
                combined = ' '.join(s)
                res.append(combined + ' ' * (maxWidth-len(combined)))
            i += 1

        return res