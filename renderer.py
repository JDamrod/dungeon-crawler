import os
from non_copyable import NonCopyable


class Renderer(NonCopyable):
    def draw(self, game_map, hero, enemies, message):
        canvas = []
        for y in range(game_map.height):
            canvas.append(list(game_map.row(y)))

        for item in game_map.items:
            canvas[item.y][item.x] = item.symbol

        alive = 0
        for enemy in enemies:
            if enemy.alive:
                canvas[enemy.y][enemy.x] = enemy.symbol
                alive += 1
        canvas[hero.y][hero.x] = hero.symbol

        os.system("cls" if os.name == "nt" else "clear")
        print("PODZIEMNY LABIRYNT\n")
        for row in canvas:
            print("".join(row))
        print(f"\nHP: {hero.hp}/{hero.max_hp}  Bron: {hero.weapon_name}  Wrogowie: {alive}")
        print("@ - Ty, E - wrog, / - bron, ! - mikstura, # - sciana, | - przejscie, K - klucz, ? - drzwi")
        print("Ruch: W/A/S/D + Enter, Wyjscie: Q.")
        print(message)
