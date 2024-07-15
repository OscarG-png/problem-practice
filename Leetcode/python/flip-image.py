class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []

        for item in image:
            res.append([
                abs(x - 1) for x in item[::-1]
            ])

        return res
