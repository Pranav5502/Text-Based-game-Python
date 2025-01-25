import time

# Game class that controls the flow of the game
class Game:
    def __init__(self):
        self.player = None
        self.is_running = True
        self.inventory = []
        self.current_location = "America"
        self.quest_progress = {}

    def start(self):
        """Starts the game, displaying a welcome message and prompting for character creation."""
        self.show_welcome_message()
        self.create_character()
        self.game_loop()

    def show_welcome_message(self):
        """Displays a welcome message."""
        print("Welcome to the Text-Based Adventure Game!")
        time.sleep(1)
        print("Embark on an adventure filled with decisions, quests, and challenges!")
        time.sleep(1)

    def create_character(self):
        """Creates a character for the player."""
        print("Enter your character's name:")
        name = input("> ").strip()

        print("Choose your character class: (1) Army man (2) Mage (3) Enemy")
        class_choice = input("> ").strip()

        if class_choice == "1":
            self.player = Character(name, " Army man", 100, 15, 10)
        elif class_choice == "2":
            self.player = Character(name, "Mage", 80, 25, 5)
        elif class_choice == "3":
            self.player = Character(name, "Enemy", 90, 20, 8)
        else:
            print("Invalid choice, defaulting to Army man.")
            self.player = Character(name, "Army man", 100, 15, 10)

        print(f"\nWelcome, {self.player.name} the {self.player.char_class}!")
        time.sleep(1)

    def game_loop(self):
        """Main game loop that runs until the game ends."""
        while self.is_running:
            self.display_location()
            self.handle_player_choice()

    def display_location(self):
        """Displays the current location and available actions."""
        print(f"\nYou are in the {self.current_location}. What would you like to do?")
        if self.current_location == "America":
            print("1) Visit the store")
            print("2) Talk to Homies")
            print("3) Head to the forest")
            print("4) View inventory")
        elif self.current_location == "forest":
            print("1) Explore deeper")
            print("2) Return to America")
        elif self.current_location == "dungeon":
            print("1) Solve the dungeon puzzle")
            print("2) Return to the America")
        else:
            print("Unknown location.")

    def handle_player_choice(self):
        """Handles the player's choice based on the current location."""
        choice = input("> ").strip()

        if self.current_location == "America":
            if choice == "1":
                self.store()
            elif choice == "2":
                self.talk_to_Homies()
            elif choice == "3":
                self.current_location = "forest"
            elif choice == "4":
                self.view_inventory()
            else:
                print("Invalid choice. Please select again.")
        elif self.current_location == "forest":
            if choice == "1":
                self.explore_forest()
            elif choice == "2":
                self.current_location = "America"
            else:
                print("Invalid choice. Please select again.")
        elif self.current_location == "dungeon":
            if choice == "1":
                self.solve_dungeon_puzzle()
            elif choice == "2":
                self.current_location = "America"
            else:
                print("Invalid choice. Please select again.")
        else:
            print("Unknown location.")

    def store(self):
        """Allows the player to visit the store and buy items."""
        print("You visit the local store.")
        print("Health Potion - 10 Gold (Restores 20 Health)")
        print("Do you want to buy a Health Potion? (y/n)")

        choice = input("> ").strip()
        if choice.lower() == "y" and self.player.gold >= 10:
            self.inventory.append("Health Potion")
            self.player.gold -= 10
            print("You bought a Health Potion!")
        elif choice.lower() == "y":
            print("You don't have enough gold.")
        else:
            print("You leave the store.")

    def talk_to_Homies(self):
        """Talk to villagers to gather information."""
        print("The Homies warn you about a dangerous monster in the forest.")
        print("They also speak of a treasure hidden in a nearby dungeon.")
        time.sleep(2)

    def view_inventory(self):
        """Displays the player's inventory."""
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        time.sleep(1)

    def explore_forest(self):
        """Allows the player to explore the forest and face challenges."""
        print("You venture deeper into the forest and encounter a wild beast!")
        print("Do you wish to fight the beast? (1) Fight (2) Run away")

        choice = input("> ").strip()

        if choice == "1":
            self.fight_beast()
        elif choice == "2":
            print("You run back to the America.")
            self.current_location = "America"
        else:
            print("Invalid choice. The beast attacks you!")
            self.fight_beast()

    def fight_beast(self):
        """Engages the player in a simple combat with a beast."""
        print("You engage the beast in battle!")
        time.sleep(1)

        if self.player.attack > 15:
            print("You defeat the beast with ease!")
            self.inventory.append("Beast Fang")
            print("You collect a Beast Fang from the fallen creature.")
        else:
            print("The beast overpowers you!")
            self.player.health -= 20
            print(f"You lose 20 health! Current health: {self.player.health}")
            if self.player.health <= 0:
                print("You have been defeated. Game Over.")
                self.is_running = False

    def solve_dungeon_puzzle(self):
        """Solves the dungeon puzzle."""
        print("You enter the dark dungeon and find a locked door with a riddle.")
        print("Riddle: I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?")

        answer = input("> ").strip().lower()

        if answer == "echo":
            print("The door opens, revealing the treasure room!")
            self.inventory.append("Treasure Chest")
        else:
            print("Incorrect answer. The door remains locked.")
            time.sleep(1)

# Character class to define the player
class Character:
    def __init__(self, name, char_class, health, attack, defense):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.attack = attack
        self.defense = defense
        self.gold = 20  # Starting gold for simplicity

    def display_stats(self):
        """Displays the character's current stats."""
        print(f"{self.name} - {self.char_class}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Gold: {self.gold}")

if __name__ == "__main__":
    # Initialize the game and start it
    game = Game()
    game.start()
