class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        hashMap = {c:set() for w in words for c in w}

        # creating the DAG
        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minLen]==w2[:minLen]:
                # if first word longer and prefix match
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    hashMap[w1[j]].add(w2[j])
                    break
        
        # true = part of current path
        # false = visited
        # neither = not visited at all
        visit = {}
        res = []

        # looking for cycles and solution string
        def dfs(c):
            if c in visit:
                return visit[c]
            
            # marking as part of current path
            visit[c] = True

            for nei in hashMap[c]:
                if dfs(nei):
                    # loop detected
                    return True

            # marking it visited
            visit[c] = False
            res.append(c)

        for c in hashMap:
            if dfs(c):
                return ''

        # reversing as we append to res from leaf nodes
        return ''.join(res[::-1])
