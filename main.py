import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []

        for color, count in kwargs.items():
            for _ in range(count):
                self.contents.append(color)

    def draw(self, number):
        if number >= len(self.contents):
            balls = self.contents
            self.contents = []
            return balls

        balls = []
        for _ in range(number):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            balls.append(ball)
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        hat_copy = Hat(**hat.kwargs)
        balls = hat_copy.draw(num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if balls.count(key) < value:
                success = False

        if success:
            success_count += 1

    return success_count / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000,
)

print(probability)
