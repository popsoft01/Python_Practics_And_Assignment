class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = point(10, 30)
print(point.x)
point.x = 15
print(point.x * point.y)
print(point.x + point.y)