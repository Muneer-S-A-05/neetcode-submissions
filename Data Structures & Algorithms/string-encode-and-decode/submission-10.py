class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return '#1'.join(strs)
        return '#0'
    def decode(self, s: str) -> List[str]:
        if s!='#0':
            return s.split('#1')
        return []
