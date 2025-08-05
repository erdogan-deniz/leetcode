class Solution:
    """
    ...
    """

    def is_nice_string(self, _str: str) -> bool:
        """
        ...
        """

        for sym in _str:
           if sym.swapcase() not in _str:
            return False

        return True

    def longest_nice_substring(self, _str: str) -> str:  # Change to `longestNiceSubstring` to pass problem
        """
        ...
        """

        right_b: int = 0

        while True:
            if right_b == len(_str, ) - 1:
                return ""

            for start_idx in range(right_b + 1, ):
                if self.is_nice_string(_str[start_idx: len(_str, ) + start_idx - right_b], ):
                    return _str[start_idx: len(_str, ) + start_idx - right_b]

            right_b += 1
