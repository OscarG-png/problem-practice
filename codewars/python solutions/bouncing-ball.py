import unittest


def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 1
    while h > window:
        h *= bounce
        if h > window:
            count += 2
    return count


class TestBouncingBall(unittest.TestCase):
    def test_bouncing_ball(self):
        self.assertEqual(bouncing_ball(2, 0.5, 1), 1)
        self.assertEqual(bouncing_ball(3, 0.66, 1.5), 3)
        self.assertEqual(bouncing_ball(30, 0.66, 1.5), 15)
        self.assertEqual(bouncing_ball(30, .75, 1.5), 21)
        self.assertEqual(bouncing_ball(-5, 0.66, 1.5), -1)


if __name__ == '__main__':
    unittest.main()
