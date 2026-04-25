class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # checking exit conditions
        if len(s)<len(t): return ''
        if s==t: return s
        
        # initilising variable
        ds, dt = {}, {}
        res,res_len = [0,-1], float('infinity')

        # creating hash table for target string
        for x in t:
            dt[x] = dt.get(x,0) + 1
        need, have = len(dt), 0
        
        l=0
        for r in range(len(s)):
            # moving right slider
            ds[s[r]] = ds.get(s[r],0) + 1
            if s[r] in dt and ds[s[r]] == dt[s[r]]:
                have+=1

            # if matching window found
            while have == need:
                # updating results
                if r-l+1 < res_len:
                    res = [l,r]
                    res_len = r-l+1
                
                # moving left slider
                ds[s[l]] -= 1
                if s[l] in dt and ds[s[l]]<dt[s[l]]:
                    have-=1
                    # reduce half only after windows freq less than required
                    # helps avoid case when freq of window greater than need
                l+=1
        l,r=res
        return s[l:r+1]