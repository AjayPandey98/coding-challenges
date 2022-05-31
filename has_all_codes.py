# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

# https://stackoverflow.com/a/287944/2557030
class BColors:
    header = '\033[95m'
    ok_blue = '\033[94m'
    ok_cyan = '\033[96m'
    ok_green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end_dc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        print(f'\n» Checking if {s} has all codes of size {k}')

        possible_combinations = 2 ** k
        print(f'\n\tThere are {possible_combinations} possible combinations')

        # Inserting and finding characters in a set is O(1)
        found = set()
        for i in range(len(s) - k + 1):
            found.add(s[i:i+k])

        has_match = f'{BColors.ok_green}It is a match{BColors.end_dc}' if len(
            found) == possible_combinations else f'{BColors.fail}It is not a match{BColors.end_dc}'
        print(f'\tFound: {found}')
        print(
            f'\t{len(found)} out of {possible_combinations} combinations of size {k};\t {has_match}')

        return len(found) == possible_combinations


def test():
    print(
        f'\n{BColors.bold}{BColors.header}» ***** Testing hasAllCodes *****{BColors.end_dc}')
    sol = Solution()
    assert sol.hasAllCodes('00110110', 2) == True
    assert sol.hasAllCodes('00110', 2) == True
    assert sol.hasAllCodes('100', 2) == False
    assert sol.hasAllCodes('0110', 2) == False
    assert sol.hasAllCodes('0110', 1) == True
    assert sol.hasAllCodes('00110110', 1) == True
    assert sol.hasAllCodes('00110110', 4) == False
    print(f'\n{BColors.bold}{BColors.ok_green}» All tests passed!{BColors.end_dc}\n')


test()
