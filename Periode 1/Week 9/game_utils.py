from time import sleep
from abc import ABC
from termcolor import colored
import random
stop_printing = False


def delay_print(message: str):
    print('')
    for char in message:
        if stop_printing:
            print(message)
            break
        print(char, end='', flush=True)
        sleep(0.015)
    print('')

def safe_input(message: str, possible_choices: list) -> int:
    while True:
        try:
            user_choice = int(input(message))
            if user_choice in possible_choices:
                return user_choice
            delay_print('Enter a possible choice!')
        except ValueError:
            delay_print('Enter an integer!')

class Entity(ABC):
    def __init__(self, name: str, strength: int, agility: int, intelligence: int, charisma: int,hp:int):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.charisma = charisma
        self.hp=hp
    def display_stats(self):
        print('')
        print(colored(f'\t{self.name}',attrs=['bold']))
        print(colored(f'HP: {self.hp}',color='light_red'))
        print(colored(f'ATTRIBUTES: ',attrs=['bold']))
        print(colored(f'  Strength: {self.strength}/10','red'))
        print(colored(f'  Agility: {self.agility}/10','green'))
        print(colored(f'  Intelligence: {self.intelligence}/10','cyan'))
        print(colored(f'  Charisma: {self.charisma}/10','light_yellow'))

class AvailableCharacter(Entity):
    def __init__(self, name: str, strength: int, agility: int, intelligence: int, charisma: int, hp:int, nickname: str, age: int, bio: str, features: str):
        super().__init__(name, strength, agility, intelligence, charisma,hp)
        self.nickname = nickname
        self.age = age
        self.bio = bio
        self.features = features
    def display_bio(self):
        self.display_stats()
        print(colored('BACKGROUND:', attrs=['bold']))
        print(self.bio)
        print(colored('FEATURES:', attrs=['bold']))
        print(self.features)


class Player(Entity):
    def __init__(self, name:str, strength:int, agility:int, intelligence:int, charisma:int, hp=100):
        super().__init__(name, strength, agility, intelligence, charisma,hp)
    def is_dead(self):
        if self.hp<0:
            quit(colored('YOU ARE DEAD','red'))
    
class Enemy(Entity):
    def __init__(self, name: str, strength: int, agility: int, intelligence: int, charisma: int, hp:int=100,negotiable:bool=True):
        super().__init__(name, strength, agility, intelligence, charisma,hp)
        self.negotiable=negotiable

import random
from time import sleep

class Combat:
    def __init__(self, player:Player, enemy:Enemy):
        self.player = player
        self.enemy = enemy
        self.win_by_negotiation=False
        self.is_lost=False

    def start_combat(self):
        delay_print(f'You are facing {self.enemy.name}!')
        self.enemy.display_stats()
        while self.player.hp > 0 and self.enemy.hp > 0:
            print("\nPlayer's status:")
            print(colored(f'HP: {self.player.hp}', 'green'))
            print("\nEnemy's status:")
            print(colored(f'HP: {self.enemy.hp}', 'red'))
            print("\nWhat will you do?")
            print(colored("1. Attack",'light_red'))
            print(colored("2. Defend",'grey'))
            if self.enemy.negotiable:
                print(colored("3. Negotiate",'yellow'))
            action = safe_input("Choose your action (1-2 or 3): ", [1, 2] + ([3] if self.enemy.negotiable else []))

            if action == 1:
                self.attack()
            elif action == 2:
                self.defend()
            elif action == 3 and self.enemy.negotiable:
                self.negotiate()

            if self.enemy.hp > 0:
                self.enemy_attack()


    def attack(self):
        player_damage = max(0, self.player.strength + random.randint(-2, 5))
        self.enemy.hp -= player_damage
        delay_print(colored(f'You attack {self.enemy.name}, dealing {player_damage} damage!','green'))

        if self.enemy.hp <= 0:
            delay_print(colored(f'{colored(self.enemy.name,attrs=['bold'])} has been defeated.','green'))

    def defend(self):
        block = random.randint(2, 5)
        delay_print(colored(f'You raise your defenses, reducing potential damage by {block} next turn!','green'))
        self.player.temp_defense = block 
    def negotiate(self):
        chance = random.randint(1, 10) + self.player.charisma - self.enemy.charisma
        if chance > 8:
            delay_print(colored(f'You successfully negotiate with {colored(self.enemy.name,attrs=['bold'])}. The fight ends peacefully!','green'))
            self.enemy.hp = 0
            self.win_by_negotiation=True
        else:
            delay_print(colored(f'{colored(self.enemy.name,attrs=['bold'])} refuses to negotiate and continues the attack!','red'))

    def enemy_attack(self):
        enemy_damage = max(0, self.enemy.strength + random.randint(-2, 5))
        if hasattr(self.player, 'temp_defense'):
            enemy_damage = max(0, enemy_damage - self.player.temp_defense) 
            del self.player.temp_defense

        self.player.hp -= enemy_damage
        delay_print(colored(f'{self.enemy.name} attacks you, dealing {enemy_damage} damage!','red'))

        if self.player.hp <= 0:
            delay_print(colored("YOU HAVE BEEN DEFEATED!",'red'))
            self.is_lost=True
        elif self.enemy.hp <= 0:
            delay_print(colored(f'YOU HAVE DEFEATED {self.enemy.name.upper}!','green'))

 
CHARACTERS_TO_CHOOSE=[
    AvailableCharacter('Edward',8,6,5,7,100,'Young Knight',24,'Edward is a descendant of an ancient line of knights who has returned to his homeland after extensive training with swordmasters. He seeks glory and adventure to restore his family’s good name. He has a strong sense of justice and is ready to help those in need.','Edward excels in combat and can influence other characters with his charisma. However, his straightforwardness can sometimes lead him into difficult situations.'),
    AvailableCharacter('Richard',7,9,6,8,100,'Bandit Leader',32,'Richard is a cunning and charismatic bandit who was once a noble knight but abandoned his honor after betrayal. He gathered a group of outlaws around him and now uses his skills for theft and manipulation.','Richard can use his charisma to manipulate other characters. His agility makes him a dangerous opponent in combat. However, his moral principles sometimes hinder him from making tough decisions.'),
    AvailableCharacter('Daniel',4,9,8,6,100,'Skilled Spy',30,'Daniel is a spy who has worked for various lords and kings. He grew up in poverty and learned to survive in harsh conditions, using his skills in stealth and manipulation. Now, he is looking for opportunities to improve his life and perhaps find his place in the world.','He skillfully avoids conflicts and can gather information without drawing attention. His agility allows him to infiltrate guarded places. However, he is not strong in combat, which makes him reliant on others.')
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
    return Player(CHARACTERS_TO_CHOOSE[choice].name,CHARACTERS_TO_CHOOSE[choice].strength,CHARACTERS_TO_CHOOSE[choice].agility,CHARACTERS_TO_CHOOSE[choice].intelligence,CHARACTERS_TO_CHOOSE[choice].charisma)
class Event():
    def __init__(self,player:Player,difficulty:str,required_skill:str=None):
        self.player=player
        self.difficulty=difficulty
        self.required_skill=required_skill
        self.DIFFICULTY_DEFINITION={
                'easy':round(random.uniform(30,60),1),
                'medium':round(random.uniform(20,40),1),
                'hard':round(random.uniform(5,25),1)
            }
        self.basic_success_chance = self.DIFFICULTY_DEFINITION[self.difficulty]
        self.COLORS={
            'agility':'green',
            'strength':'red',
            'intelligence':'cyan',
            'charisma':'yellow'
        }
        self.PLAYER_SKILL={
            'agility':self.player.agility,
            'strength':self.player.strength,
            'intelligence':self.player.intelligence,
            'charisma':self.player.charisma
        }
    def define_succes_including_skills(self)->float:
        success = float(self.PLAYER_SKILL[self.required_skill]*5)
        self.basic_success_chance+=success
        return success
    def take_a_try(self)->bool:
        return self.basic_success_chance>random.uniform(0,100)