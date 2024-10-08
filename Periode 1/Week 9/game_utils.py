from time import sleep
from pynput import keyboard
from abc import ABC
from termcolor import colored
import random
stop_printing = False

def on_press(key):
    global stop_printing
    if key == keyboard.Key.enter:
        stop_printing = True

def delay_print(message: str):
    global stop_printing
    for char in message:
        if stop_printing:
            print(message)
            break
        print(char, end='', flush=True)
        sleep(0.04)
    print('')
    stop_printing = False

def safe_input(message: str, possible_choices: list) -> int:
    while True:
        try:
            user_choice = int(input(message))
            if user_choice in possible_choices:
                return user_choice
            delay_print('Enter a possible choice!')
        except ValueError:
            delay_print('Enter an integer!')

listener = keyboard.Listener(on_press=on_press)
listener.start()

class Entity(ABC):
    def __init__(self, name: str, strength: int, agility: int, intelligence: int, charisma: int,hp:int,armor:int):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.charisma = charisma
        self.hp=hp
        self.armor=armor
class AvailableCharacter(Entity):
    def __init__(self, name: str, strength: int, agility: int, intelligence: int, charisma: int, hp:int, armor:int, nickname: str, age: int, bio: str, features: str):
        super().__init__(name, strength, agility, intelligence, charisma)
        self.nickname = nickname
        self.age = age
        self.bio = bio
        self.features = features

    def display_attributes(self):
        print(colored(f'\tStrength: {self.strength}/10','red'))
        print(colored(f'\tAgility: {self.agility}/10','green'))
        print(colored(f'\tIntelligence: {self.intelligence}/10','cyan'))
        print(colored(f'\tCharisma: {self.charisma}/10','light_yellow'))
    def display_bio(self):
        print(colored(f'{self.name} - {self.nickname}', attrs=['bold']))
        print(f'AGE: {self.age} years')
        print('ATTRIBUTES')
        self.display_attributes()
        print(colored('BACKGROUND:', attrs=['bold']))
        print(self.bio)
        print(colored('FEATURES:', attrs=['bold']))
        print(self.features)


class Player(AvailableCharacter):
    def __init__(self, name:str, strength:int, agility:int, intelligence:int, charisma:int, nickname:str, age:int, bio:str, features:str, hp=100, armor=0, items=None):
        super().__init__(name, strength, agility, intelligence, charisma, nickname, age, bio, features)
        self.hp = hp
        self.armor = armor
        self.items = items or []

    def display_stats(self):
        print(colored(f'HP: {self.hp}', 'light_red'))
        print(colored(f'ARMOR: {self.armor}', 'grey'))
        print('ITEMS:', ', '.join(map(str, self.items)) if self.items else 'No items')
        print('')
        print('ATTRIBUTES: ')
        self.display_attributes()
class Enemy(Entity):
    def __init__(self, name: str, strength: int, agility: int, intelligence: int, charisma: int, negotiable:bool=True):
        super().__init__(name, strength, agility, intelligence, charisma)
        self.negotiable=negotiable

class Combat:
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy

    def start_combat(self):
        delay_print(f'You are facing {self.enemy.name}!')
        while self.player.hp > 0 and self.enemy.hp > 0:
            print("\nWhat will you do?")
            print("1. Attack")
            print("2. Defend")
            if self.enemy.negotiable:
                print("3. Negotiate")
            action = safe_input("Choose your action (1-2 or 3): ", [1, 2] + ([3] if self.enemy.negotiable else []))
            
            if action == 1:
                self.attack()
            elif action == 2:
                self.defend()
            elif action == 3:
                self.negotiate()
            
            if self.enemy.hp > 0:
                self.enemy_attack()

        if self.player.hp <= 0:
            delay_print("You have been defeated!")
        elif self.enemy.hp <= 0:
            delay_print(f"You have defeated {self.enemy.name}!")

    def attack(self):
        player_damage = max(0, self.player.strength + random.randint(-2, 2) - self.enemy.armor)
        self.enemy.hp -= player_damage
        delay_print(f'You attack {self.enemy.name}, dealing {player_damage} damage!')

        if self.enemy.hp <= 0:
            delay_print(f'{self.enemy.name} has been defeated.')

    def defend(self):
        block = random.randint(2, 5)
        self.player.armor += block
        delay_print(f'You raise your defenses, increasing armor by {block}!')

    def negotiate(self):
        chance = random.randint(1, 10) + self.player.charisma - self.enemy.charisma
        if chance > 8:
            delay_print(f'You successfully negotiate with {self.enemy.name}. The fight ends peacefully!')
            self.enemy.hp = 0
        else:
            delay_print(f'{self.enemy.name} refuses to negotiate and continues the attack!')

    def enemy_attack(self):
        enemy_damage = max(0, self.enemy.strength + random.randint(-2, 2) - self.player.armor)
        self.player.hp -= enemy_damage
        delay_print(f'{self.enemy.name} attacks you, dealing {enemy_damage} damage!')
        if enemy_damage > 0:
            self.player.armor = max(0, self.player.armor - 1)  # Armor degrades after taking damage

def combat(player: Player, enemy: Enemy):
    delay_print(f'You are facing {enemy.name}!')
    while player.hp > 0 and enemy.hp > 0:
        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Defend")
        if enemy.negotiable:
            print("3. Negotiate")
        
        action = safe_input("Choose your action (1-2 or 3): ", [1, 2] + ([3] if enemy.negotiable else []))

        if action == 1:
            player_attack(player, enemy)
        elif action == 2:
            defend(player, enemy)
        elif action == 3 and enemy.negotiable:
            negotiate(player, enemy)

        if enemy.hp > 0:
            enemy_turn(player, enemy)

        print("\nPlayer's status:")
        player.display_stats()
        print("\nEnemy's status:")
        print(colored(f'HP: {enemy.hp}', 'light_red'))

    if player.hp <= 0:
        delay_print("You have been defeated!")
    elif enemy.hp <= 0:
        delay_print(f"You have defeated {enemy.name}!")

def player_attack(player: Player, enemy: Enemy):
    damage = max(player.strength - enemy.armor, 0) + random.randint(0, 5)
    delay_print(f"You attack {enemy.name} and deal {damage} damage!")
    enemy.hp -= damage

def defend(player: Player, enemy: Enemy):
    defense = player.armor + random.randint(1, 5)
    delay_print(f"You prepare to defend, increasing your defense by {defense}!")

def negotiate(player: Player, enemy: Enemy):
    success_chance = player.charisma + random.randint(0, 10) - enemy.charisma
    if success_chance > 5:
        delay_print(f"You successfully negotiate with {enemy.name}. The fight ends peacefully.")
        enemy.hp = 0
    else:
        delay_print(f"{enemy.name} refuses to negotiate!")

def enemy_turn(player: Player, enemy: Enemy):
    damage = max(enemy.strength - player.armor, 0) + random.randint(0, 5)
    delay_print(f"{enemy.name} attacks you and deals {damage} damage!")
    player.hp -= damage

 
CHARACTERS_TO_CHOOSE=[
    AvailableCharacter('Edward',8,6,5,7,100,0,'Young Knight',24,'Edward is a descendant of an ancient line of knights who has returned to his homeland after extensive training with swordmasters. He seeks glory and adventure to restore his family’s good name. He has a strong sense of justice and is ready to help those in need.','Edward excels in combat and can influence other characters with his charisma. However, his straightforwardness can sometimes lead him into difficult situations.'),
    AvailableCharacter('Liam',6,8,7,5,100,0,'Master Weaponsmith',28,'Liam is a talented blacksmith who grew up in a village dominated by men. Since childhood, he helped his father in the forge and learned not only to create weapons but also to fight. He wants to prove that a man can be not only a blacksmith but also a great warrior.','He possesses unique skills in weapon creation and modification. His agility helps him avoid conflicts and improves his performance in battles. However, his low charisma may hinder interactions with others.'),
    AvailableCharacter('Richard',7,9,6,8,100,0,'Bandit Leader',32,'Richard is a cunning and charismatic bandit who was once a noble knight but abandoned his honor after betrayal. He gathered a group of outlaws around him and now uses his skills for theft and manipulation.','Richard can use his charisma to manipulate other characters. His agility makes him a dangerous opponent in combat. However, his moral principles sometimes hinder him from making tough decisions.'),
    AvailableCharacter('Gregory',3,4,9,7,100,0,'Wise Healer',45,'Gregory is a well-known healer who has devoted his life to studying herbs and healing. He possesses deep knowledge of medicine and the history of his people. His wisdom and experience make him an important ally.','He can heal the wounded and provide useful advice, which can help the player in difficult situations. However, his low physical attributes make him vulnerable in battles.'),
    AvailableCharacter('Daniel',4,9,8,6,100,0,'Skilled Spy',30,'Daniel is a spy who has worked for various lords and kings. He grew up in poverty and learned to survive in harsh conditions, using his skills in stealth and manipulation. Now, he is looking for opportunities to improve his life and perhaps find his place in the world.','He skillfully avoids conflicts and can gather information without drawing attention. His agility allows him to infiltrate guarded places. However, he is not strong in combat, which makes him reliant on others.')
    ]

def CharacterChoose():
    while True:
        for i in range (len(CHARACTERS_TO_CHOOSE)):
            print(colored(f'{i+1}. {CHARACTERS_TO_CHOOSE[i].name} - {CHARACTERS_TO_CHOOSE[i].nickname}',attrs=['bold']))
        choice = safe_input('Choose the character to get more info about him\n',range(1,len(CHARACTERS_TO_CHOOSE)+1)) - 1
        print('\n')
        CHARACTERS_TO_CHOOSE[choice].display_bio()
        print('\n')
        print('Would you like to choose this character?')
        print('1. Yes\n2. No, I would like to pick another one')
        usr = safe_input('',[1,2])
        if usr == 1:
            break
    return Player(CHARACTERS_TO_CHOOSE[choice].name,CHARACTERS_TO_CHOOSE[choice].strength,CHARACTERS_TO_CHOOSE[choice].agility,CHARACTERS_TO_CHOOSE[choice].intelligence,CHARACTERS_TO_CHOOSE[choice].charisma,CHARACTERS_TO_CHOOSE[choice].nickname,CHARACTERS_TO_CHOOSE[choice].age,CHARACTERS_TO_CHOOSE[choice].bio,CHARACTERS_TO_CHOOSE[choice].features)