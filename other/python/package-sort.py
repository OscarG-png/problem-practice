import unittest


def package_sort(width: int, height: int, length: int, mass: int) -> str:
    volume = width * height * length
    bulky = (width >= 150 or height >= 150 or length >= 150) or (volume > 1000000)

    if bulky and mass >= 20:
        return "REJECTED"
    elif bulky or mass >= 20:
        return "SPECIAL"
    else:
        return "STANDARD"


class TestPackageSort(unittest.TestCase):
    def test_package(self):
        self.assertEqual(package_sort(160, 70, 70, 10), "SPECIAL")
        self.assertEqual(package_sort(120, 100, 100, 10), "SPECIAL")
        self.assertEqual(package_sort(90, 90, 118, 10), "STANDARD")
        self.assertEqual(package_sort(120, 100, 50, 30), "SPECIAL")
        self.assertEqual(package_sort(80, 110, 80, 70), "SPECIAL")
        self.assertEqual(package_sort(70, 80, 90, 10), "STANDARD")
        self.assertEqual(package_sort(100, 120, 60, 19), "STANDARD")
        self.assertEqual(package_sort(150, 70, 70, 10), "SPECIAL")
        self.assertEqual(package_sort(120, 100, 100, 10), "SPECIAL")
        self.assertEqual(package_sort(90, 90, 118, 10), "STANDARD")
        self.assertEqual(package_sort(120, 100, 110, 20), "REJECTED")
        self.assertEqual(package_sort(80, 110, 80, 70), "SPECIAL")
        self.assertEqual(package_sort(70, 80, 90, 10), "STANDARD")
        self.assertEqual(package_sort(100, 150, 60, 30), "REJECTED")


if __name__ == '__main__':
    unittest.main()
