"""
Solution: two pointers.

Time complexity: O(n).
Space complexity: O(1).
"""

class Solution:
    """
    ...
    """

    def max_area(self, lines_heights: list[int]) -> int:
        """
        ...
        """

        area: int = 0
        left_idx: int = 0
        right_idx: int = len(lines_heights, ) - 1

        while left_idx < right_idx:
            idx_diff: int = right_idx - left_idx
            loc_area: int = min(
                lines_heights[left_idx],
                lines_heights[right_idx],
            ) * idx_diff
            area = max(area, loc_area, )

            if lines_heights[left_idx] < lines_heights[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1

        return area
