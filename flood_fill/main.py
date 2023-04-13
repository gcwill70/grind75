class Solution:
    def fill(self, image, sr, sc, color, old):
        if sr < 0 or sr >= len(image):
            return
        if sc < 0 or sc >= len(image[sr]):
            return
        if image[sr][sc] != old:
            return
        image[sr][sc] = color
        self.fill(image, sr + 1, sc, color, old)
        self.fill(image, sr - 1, sc, color, old)
        self.fill(image, sr, sc - 1, color, old)
        self.fill(image, sr, sc + 1, color, old)

    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        old = image[sr][sc]
        if old == color:
            return image
        self.fill(image, sr, sc, color, old)
        return image
