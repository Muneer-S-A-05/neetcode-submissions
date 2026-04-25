class Solution:

    def encode(self, strs: List[str]) -> str:
        return '#-'.join(strs) if strs else '#0'
    def decode(self, s: str) -> List[str]:
        return s.split('#-') if s!='#0' else []
