class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return '#-'.join(strs)
        else:
            return '#0'
    def decode(self, s: str) -> List[str]:
        if s!='#0':
            return s.split('#-')
        else:
            return []
