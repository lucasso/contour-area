import unittest

def area(s : str) -> int:
    path = []
    x = 0
    y = 0
    area = 0

    for ch in s:
        if ch == 'L':
            x -= 1
        elif ch == 'R':
            x += 1
        elif ch == 'U' and y < 0:
            area += path.pop() - x
            y += 1
        elif ch == 'D' and y > 0:
            area += x - path.pop()
            y -= 1
        elif ch == 'U' and y >= 0:
            path.append(x)
            y += 1
        elif ch == 'D' and y <= 0:
            path.append(x)
            y -= 1
        else:
            raise RuntimeError(f"Unrecognized character {ch}")

    if x != 0 or y != 0:
        raise RuntimeError(f"Finished in wrong coordinates x:{x} y:{y}")

    return abs(area)


class TestContour(unittest.TestCase):

    def _test_with_all_staring_points(self, s, expected_area):
        for split_point in range(len(s)):
            s_shifted = s[split_point:]+s[0:split_point]
            self.assertEqual(area(s_shifted), expected_area)

    def test_simplest(self):
        # *
        self._test_with_all_staring_points("URDL", 1)

    def test_hole(self):
        # ***
        # * *
        self._test_with_all_staring_points("RRRDDLULDLUU", 5)

    def test_hole_in_a_hole(self):
        # ******
        # **   *
        # ** * *
        # ** * *
        # ** ***
        s = "RRRRRRDDDDDLLLUUURDDRUUULLLDDDDLLUUUUU"
        self._test_with_all_staring_points(s, 22)

    def test_different_directions(self):
        # **** ******
        # *        *
        # * ****** *
        # * * * ** **
        # *   * ** **
        # *****    **
        # ***********
        s = "RRRRDLLLDDDDRRRUULDLUURRRRRRDDDLLUULDDDRRRRUUUUULLLLURRRRRRDLDDRDDDDLLLLLLLLLLLUUUUUUU"
        self._test_with_all_staring_points(s, 51)


    def test_blazej_case(self):
        s = "RRRRRRRRURRRDDDDDDDLLUULLLLLDDRRDRDDDLLDDLLUUUUUUUULLUUULU"
        self._test_with_all_staring_points(s, 69)

if __name__ == '__main__':
    unittest.main()
