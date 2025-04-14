import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents = []
            return drawn
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_balls)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_counts = {color: drawn_balls.count(color) for color in expected_balls}
        
        if all(drawn_counts[color] >= expected_balls[color] for color in expected_balls):
            success_count += 1
    
    return success_count / num_experiments
