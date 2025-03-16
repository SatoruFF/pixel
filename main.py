import pyxel
import time
class ChronoCat:
    def __init__(self):
        pyxel.init(160, 120, title="Chrono: Time Heist")
        pyxel.load("./assets/main_pers.pyxres")
        self.cat_x = 10
        self.cat_y = 80
        self.time_energy = 100
        self.platforms = [(0, 100, 160, 10), (50, 70, 60, 10), (120, 50, 40, 10)]
        self.time_slow = False
        self.energy_recovery_timer = 0 
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.cat_x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.cat_x += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.cat_y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.cat_y += 1
        
        if pyxel.btn(pyxel.KEY_SPACE) and self.time_energy > 0:
            self.time_slow = True
            self.time_energy -= 1
            self.energy_recovery_timer = 0
        else:
            self.time_slow = False

        # Восстановление энергии (раз в 30 кадров ≈ 0.5 сек при 60 FPS)
        self.energy_recovery_timer += 1
        if self.energy_recovery_timer >= 30:
            if self.time_energy < 100:
                self.time_energy += 1
            self.energy_recovery_timer = 0 

    def draw(self):
        pyxel.cls(0)
        for plat in self.platforms:
            pyxel.rect(plat[0], plat[1], plat[2], plat[3], 8)
        # pyxel.rect(self.cat_x, self.cat_y, 8, 8, 7)
        pyxel.blt(self.cat_x, self.cat_y, 0, 0, 0, 8, 8, 0)
        pyxel.text(10, 10, f"Time Energy: {self.time_energy}", 7)

if __name__ == "__main__":
    ChronoCat()