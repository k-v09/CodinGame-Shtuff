import sys
from collections import defaultdict
import heapq

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def squared_magnitude(self):
        return self.x**2 + self.y**2

    def normalize(self):
        mag = self.squared_magnitude()**0.5
        if mag == 0:
            return Vector2D(0, 0)  
        return Vector2D(self.x / mag, self.y / mag)

class Entity:
    def __init__(self, id, position):
        self.id = id
        self.position = position

class Human(Entity):
    pass

class Zombie(Entity):
    def __init__(self, id, position, next_position):
        super().__init__(id, position)
        self.next_position = next_position

class Game:
    def __init__(self):
        self.humans = {}
        self.zombies = {}
        self.distance_cache = defaultdict(dict)
        self.ash_position = Vector2D(0, 0)
        self.urgent_humans = []

    def update_state(self):
        x, y = map(int, input().split())
        self.ash_position = Vector2D(x, y)
        self.humans.clear()
        self.zombies.clear()
        self.urgent_humans = []

        human_count = int(input())
        for _ in range(human_count):
            human_id, human_x, human_y = map(int, input().split())
            self.humans[human_id] = Human(human_id, Vector2D(human_x, human_y))

        zombie_count = int(input())
        for _ in range(zombie_count):
            zombie_id, zombie_x, zombie_y, zombie_next_x, zombie_next_y = map(int, input().split())
            self.zombies[zombie_id] = Zombie(zombie_id, Vector2D(zombie_x, zombie_y), Vector2D(zombie_next_x, zombie_next_y))

        self._update_urgent_humans()

    def _update_urgent_humans(self):
        for human in self.humans.values():
            nearest_zombie = min(
                self.zombies.values(),
                key=lambda z: (z.position - human.position).squared_magnitude()
            )
            time_for_zombie = ((nearest_zombie.position - human.position).squared_magnitude() ** 0.5) / 400
            time_for_ash = ((self.ash_position - human.position).squared_magnitude() ** 0.5) / 1000

            if time_for_zombie < time_for_ash:
                heapq.heappush(self.urgent_humans, (time_for_zombie, human.id))

    def predict_n_turns(self, n):
        predicted_zombies = {}
        for zombie in self.zombies.values():
            direction = (zombie.next_position - zombie.position).normalize()
            predicted_pos = zombie.position + direction * (400 * n)
            predicted_zombies[zombie.id] = Zombie(zombie.id, predicted_pos, predicted_pos)
        return predicted_zombies

    def find_best_position(self):
        if self.urgent_humans:
            _, urgent_human_id = heapq.heappop(self.urgent_humans)
            return self.humans[urgent_human_id].position

        weighted_position = Vector2D(0, 0)
        total_weight = 0

        for human in self.humans.values():
            distance = max((self.ash_position - human.position).squared_magnitude(), 1)  
            weight = 1 / distance
            weighted_position += human.position * weight
            total_weight += weight

        for zombie in self.zombies.values():
            distance = max((self.ash_position - zombie.position).squared_magnitude(), 1)  
            weight = 2 / distance  
            weighted_position += zombie.position * weight
            total_weight += weight

        if total_weight == 0:
            return self.ash_position  

        return weighted_position * (1 / total_weight)

    def execute_turn(self):
        target = self.find_best_position()
        print(f"{int(target.x)} {int(target.y)}")

game = Game()


while True:
    game.update_state()
    game.execute_turn()