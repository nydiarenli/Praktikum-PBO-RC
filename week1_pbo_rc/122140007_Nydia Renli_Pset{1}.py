class BattleBot:
    def __init__(self, name, health, attack_power, armor):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.armor = armor

    def show_bot_info(self):
        print(f"Bot Name     : {self.name}")
        print(f"Health       : [{self.health}]")
        print(f"Attack Power : [{self.attack_power}]")
        print(f"Armor        : [{self.armor}]")

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}")

        enemy.health -= int((self.attack_power / enemy.armor))
        print(f"{enemy.name}'s Health  -{int(self.attack_power / enemy.armor)}")
        print(f"{enemy.name}'s Health[{enemy.health}] \n")

        enemy.counter_attack(self)

    def counter_attack(self, enemy):
        print(f"{self.name} counter attacks {enemy.name}")

        enemy.health -= int((self.attack_power / enemy.armor))
        print(f"{enemy.name}'s Health  -{int(self.attack_power / enemy.armor)}")
        print(f"{enemy.name}'s Health[{enemy.health}]")
            

class BattleArena:
    def __init__(self):
        self.bot_list = []

    def add_bot(self, bot):
        self.bot_list.append(bot)

    def show_bot_list(self):
        print("=== BOT LIST ===")
        print()
        for bot in self.bot_list:
            bot.show_bot_info()
            print()

    def choose_bots(self):
        choose_bot = input("Choose your bot (write down the bot's name): ")
        choose_enemy = input("Choose your enemy (write down the enemy's name): ")

        chosen_bot = None
        chosen_enemy = None

        for bot in self.bot_list:
            if bot.name.lower() == choose_bot.lower():
                chosen_bot = bot
            if bot.name.lower() == choose_enemy.lower():
                chosen_enemy = bot

        print()
        if chosen_bot and chosen_enemy:
            print(f"You chose {chosen_bot.name} as your bot")
            print(f"You chose {chosen_enemy.name} as your enemy")
            print("Let's start!\n\n")
            return chosen_bot, chosen_enemy
        else:
            print("Invalid bot or enemy!")

    def start_battle(self):
        chosen_bot, chosen_enemy = self.choose_bots()

        winner = None
        while chosen_bot.health > 0 and chosen_enemy.health > 0:
            input_option = int(input("Press 1 to attack: "))

            print()
            if input_option == 1:
                chosen_bot.attack(chosen_enemy)
                print()
            else:
                print("Invalid input!")
                break

            if chosen_bot.health == 0:
                winner = chosen_enemy
            else:
                winner = chosen_bot

        print(f"==== THE WINNER IS ====")
        print(f"\t{winner.name}")


if __name__ == "__main__":
    arena = BattleArena()

    bot1 = BattleBot("Bot1", 1000, 500, 10)
    bot2 = BattleBot("Bot2", 500, 250, 5)
    bot3 = BattleBot("Bot3", 760, 320, 6)

    arena.add_bot(bot1)
    arena.add_bot(bot2)
    arena.add_bot(bot3)

    arena.show_bot_list()
    arena.start_battle()
