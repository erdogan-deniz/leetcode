"""
Solution: prefix sum and hash map.

`pref_sum` - это массив (дискретный аналог интеграла).
`k` - это некий `правый` подмассив, который занимает пространство массива, его
сумма равна `k`.
`pref_sum - k` - это некий `левый` подмассив, который занимает пространство
массива существует при условии, что вы нашли `k`.
Если `pref_sum` встречается снова, значит существует подмассив, которого толкает
подмассив `pref_sum - k` с суммой элементов равной `k`.

Time complexity: O(n).
Space complexity: O(n).
"""


class Solution:
    """
    ...
    """

    def subarray_sum(
        self,
        nums: list[int],
        k: int
    ) -> int:
        """
        ...
        """

        pref_sum: int = 0
        subarr_cnt: int = 0
        # Случай, когда `pref_sum` равен `k`:
        pref_sum_cnt: dict[int, int] = {0: 1, }

        for num in nums:
            pref_sum += num

            if (pref_sum - k) in pref_sum_cnt:  # Существует подмассив с суммой
                                                # равной `k`?
                subarr_cnt += pref_sum_cnt[pref_sum - k]  # Количество таких
                                                          # подмассивов

            pref_sum_cnt[pref_sum] = pref_sum_cnt.get(pref_sum, 0, ) + 1

        return subarr_cnt
