class Solution:
    def defangIPaddr(self, address: str) -> str:
        temp = address.split('.')
        result = '[.]'.join(temp)
        return result
