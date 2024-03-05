import random

class Robot:
    def __init__(self, nama, hp, serangan):
        self.nama = nama
        self.hp = hp
        self.serangan = serangan

    def serang_musuh(self, musuh):
        if random.random() < 0.8: 
            musuh.hp -= self.serangan
            print(f"{self.nama} menyerang {musuh.nama} dengan kekuatan {self.serangan}!")
        else:
            print(f"{self.nama} meleset dalam serangannya!")

    def pulihkan_kesehatan(self):
        self.hp += 50
        print(f"{self.nama} pulih sebanyak 50 poin kesehatan.")

class Permainan:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.putaran = 1

    def mainkan_putaran(self):
        print(f"Putaran-{self.putaran}")
        print(f"{self.robot1.nama}|{self.robot1.hp}|{self.robot1.serangan}|")
        print(f"{self.robot2.nama}|{self.robot2.hp}|{self.robot2.serangan}|")

        aksi1 = int(input(f"{self.robot1.nama}, Pilih aksi:\n1 Serang\n2 Bertahan\n3 Menyerah\n"))
        aksi2 = int(input(f"{self.robot2.nama}, Pilih aksi:\n1 Serang\n2 Bertahan\n3 Menyerah\n"))

        if aksi1 == 1:
            self.robot1.serang_musuh(self.robot2)
        elif aksi1 == 2:
            self.robot1.pulihkan_kesehatan()
        elif aksi1 == 3:
            print(f"{self.robot1.nama} menyerah!")
            return

        if aksi2 == 1:
            self.robot2.serang_musuh(self.robot1)
        elif aksi2 == 2:
            self.robot2.pulihkan_kesehatan()
        elif aksi2 == 3:
            print(f"{self.robot2.nama} menyerah!")
            return

        self.putaran += 1

        if self.robot1.hp <= 0:
            print(f"{self.robot2.nama} menang!")
        elif self.robot2.hp <= 0:
            print(f"{self.robot1.nama} menang!")
        else:
            self.mainkan_putaran()

robot1 = Robot("Atreus", 500, 10)
robot2 = Robot("Daedalus", 750, 8)

permainan = Permainan(robot1, robot2)
permainan.mainkan_putaran()
