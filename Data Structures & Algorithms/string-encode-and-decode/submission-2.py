class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "--1"
        if strs == [""]:
            return "--2"
        return "&^&".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "--1":
            return []
        if s == "--2":
            return [""]
        return s.split("&^&")