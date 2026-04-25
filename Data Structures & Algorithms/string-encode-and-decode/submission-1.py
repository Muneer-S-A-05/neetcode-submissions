class Solution:

    def encode(self, strs: List[str]) -> str:
        return '#00'.join(strs) if strs else '#20'
    def decode(self, s: str) -> List[str]:
        return s.split('#00') if s!='#20' else []
