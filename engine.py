from commands import Command
from enemy import Enemy
from game_map import Map
from hero import Hero
from input_handler import InputHandler
from non_copyable import NonCopyable
from potion import Potion
from renderer import Renderer
from weapon import Weapon
from key import Key

LEVEL_ONE = [
    "####################",
    "#@.....#...........#",
    "#......#....E......#",
    "#..S...........P...#",
    "#......#...........#",
    "###.####.#####.#####",
    "#..E.....#.......E.#",
    "#.......P#.........|",
    "####################",
]

LEVEL_TWO = [
    "####################",
    "#K...E...#.........#",
    "#######..#..E......#",
    "#........#....######",
    "#P.......#.........#",
    "#........?.........#",
    "#######..#.......E.#",
    "#@......E#.........#",
    "####################",
]
MOVES = {
    Command.UP: (0, -1),
    Command.DOWN: (0, 1),
    Command.LEFT: (-1, 0),
    Command.RIGHT: (1, 0),
}


class Engine(NonCopyable):
    def __init__(self):
        self.__input = InputHandler()
        self.__renderer = Renderer()
        self.__hero = None
        self.__enemies = []
        self.__map = None
        self.__key = None
        self.__level = 1
        self.__exit = None
        self.__load(LEVEL_ONE)
        self.__message = "Zabij wszystkich potworow!"

    def run(self):
        while self.__hero.alive:
            self.__draw()
            command = self.__input.read()
            if command is Command.QUIT:
                return
            if command in MOVES:
                dx, dy = MOVES[command]
                self.__message = ""
                self.__hero_turn(dx, dy)
                self.__enemies_turn()
            
            if self.__level == 1 and (self.__hero.x, self.__hero.y) == self.__exit:
                if self.__enemies_left() == 0:
                    self.__level = 2
                    self.__load(LEVEL_TWO)
                else: 
                    self.__message = "Musisz zabic wszystkich wrogow"
                    self.__hero.move_to(self.__exit[0] - 1, self.__exit[1])

            if self.__level == 2 and self.__enemies_left() == 0:
                break   

        self.__draw()

        
        if self.__hero.alive:
            print("WYGRALES!")
        else:
            print("PRZEGRALES...")

    def __load(self, layout):
        self.__exit = None
        items = []
        rows = []
        for y in range(len(layout)):
            line = layout[y]
            for x in range(len(line)):
                ch = line[x]
                if ch == "@" and self.__hero is None:
                    self.__hero = Hero(x, y)
                elif ch == "@" and self.__hero is not None:
                    self.__hero.move_to(x, y)
                elif ch == "E":
                    self.__enemies.append(Enemy(x, y))
                elif ch == "S":
                    items.append(Weapon("Miecz", x, y, 4))
                elif ch == "P":
                    items.append(Potion("Mikstura", x, y, 15))
                elif ch == "K":
                    items.append(Key("Klucz", x, y))
                elif ch == "|":
                    self.__exit = (x, y)
            for mark in "@ESPK":
                line = line.replace(mark, ".")
            rows.append(line)
        self.__map = Map(rows, items)

    def __draw(self):
        self.__renderer.draw(self.__map, self.__hero, self.__enemies, self.__message)

    def __enemies_left(self):
        count = 0
        for enemy in self.__enemies:
            if enemy.alive:
                count += 1
        return count

    def __enemy_at(self, x, y):
        for enemy in self.__enemies:
            if enemy.alive and enemy.x == x and enemy.y == y:
                return enemy
        return None

    def __hero_turn(self, dx, dy):
        x = self.__hero.x + dx
        y = self.__hero.y + dy
        target = self.__enemy_at(x, y)
        if target is not None:
            self.__hero.attack(target)
            self.__message = f"Uderzasz: {self.__hero.attack_power()} obrazen"

        elif not self.__map.is_wall(x, y):
            if self.__map.is_door(x, y):
                if self.__hero.key is not None:
                    self.__map.open_door(x, y)
                    self.__hero.move_to(x, y)
                else:
                    self.__message = "Nie masz klucza"
            else:
                self.__hero.move_to(x, y)
                item = self.__map.item_at(x, y)
                if item is not None:
                    item.on_pickup(self.__hero)
                    self.__map.remove_item(item)
                    self.__message = f"Podniosles: {item.name}"

    def __enemies_turn(self):
        for enemy in self.__enemies:
            if not enemy.alive:
                continue
            x, y = enemy.next_step(self.__hero)
            if x == self.__hero.x and y == self.__hero.y:
                enemy.attack(self.__hero)
            elif not self.__map.is_wall(x, y) and self.__enemy_at(x, y) is None and not self.__map.is_door(x,y):
                enemy.move_to(x, y)
