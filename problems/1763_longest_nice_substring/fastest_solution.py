class Solution:
    """
    ...
    """

    def longest_nice_substring(self, _str: str) -> str:  # Change to `longestNiceSubstring` to pass problem
        """
        ...
        """

        set_str: set = set(_str, )

        for idx in range(len(_str, ), ):
            if (_str[idx].upper() not in set_str) or (_str[idx].lower() not in set_str):
                l_str: str = self.longest_nice_substring(_str[: idx], )  # Change to `longestNiceSubstring` to pass problem
                r_str: str = self.longest_nice_substring(_str[idx+1: ], )  # Change to `longestNiceSubstring` to pass problem

                return l_str if len(l_str, ) >= len(r_str, ) else r_str

        return _str
