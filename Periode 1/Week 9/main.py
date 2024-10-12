from game_utils import *
from os import system
print('CHOOSE YOUR CHARACTER: ')
player = CharacterChoose()
SKILLS_COLORS={
    'agility':'green',
    'strength':'red',
    'intelligence':'cyan',
    'charisma':'yellow'
}
system('cls')
system('clear')
delay_print('LORE: ')
delay_print('After many years of wandering, you have returned to your homeland, spurred by strange rumors circulating among the local peasants about unusual events occurring in the abandoned castle on the high hill. Many associate the disappearances of local residents with this place, while the corrupt royal guards turn a blind eye to the situation.')
sleep(1)
delay_print('The only hope is you.')
sleep(1)
#CASTLE WALL
delay_print('Late night. There is snow all around. You climb the hill and stand at the castle walls. How would you get inside?')
print('')
while True:
    event=Event(player,'easy','agility')
    print(f'1. Climb the wall [{event.basic_success_chance}%] {colored(f'(+{event.define_succes_including_skills()}% DUE TO {event.required_skill.upper()} SKILLS)',color=event.COLORS[event.required_skill])}\n2. Go around the castle and try to find another entrance')
    castle_wall=safe_input('',[1,2])
    if castle_wall == 1:
        if event.take_a_try():
            delay_print('You easily climb the wall and go down the stairs on the other side')
            sleep(1)
            delay_print("You go down the stairs and suddenly a skeleton appears from around the corner. He has a sword and helmet and definitely doesn't look friendly. You have no other option but fight.")
            break
        else:
            delay_print('You clumsily climb the wall, but suddenly you slip and fall')
            delay_print(colored('-20 HP','light_red'))
            player.hp-=20
            player.is_dead()
    elif castle_wall == 2:
        delay_print('You go to the other side of castle')
        sleep(1)
        delay_print('You see that the other side of castle is partially destroyed and there is a big hole in the wall, but this passage is guarded by a skeleton with sword and helmet. You have no other option but fight.')
        break
print('')
skeleton=Enemy('Skeleton',1,0,0,0,30,False)
combat=Combat(player,skeleton)
combat.start_combat()
if combat.is_lost:quit()

# Event: Entering the Castle
delay_print('You enter the dark castle. The walls are cold and the air is thick with the smell of decay. Suddenly, a loud noise echoes through the halls...')
sleep(1)

# Event 1: Trap Room - Use Strength
delay_print('You find yourself in a room with a large door that suddenly slams shut behind you. There are chains hanging from the ceiling, and the floor begins to rise slowly.')
delay_print('The room is about to be crushed. You need to find a way to stop the mechanism before it’s too late.')
event = Event(player, 'medium', 'strength')
print(f'1. Use your strength to try to pull the chains and stop the trap [{event.basic_success_chance}%] {colored(f"(+{event.define_succes_including_skills()}% DUE TO {event.required_skill.upper()} SKILLS)", color=event.COLORS[event.required_skill])}\n2. Search the room for a switch or lever')
trap_room = safe_input('', [1, 2])

if trap_room == 1:
    if event.take_a_try():
        delay_print('You manage to break the chains with your raw strength, stopping the trap just in time.')
        delay_print('You breathe a sigh of relief but know this is only the beginning.')
    else:
        delay_print('You pull on the chains with all your might, but the pressure becomes too much. The ceiling crushes you.')
        quit(colored('You are dead!', 'light_red'))
else:
    delay_print('You search the room and find a lever hidden behind a tapestry. You pull it, and the room resets to its original state.')
    delay_print('You move forward, ready for whatever awaits next.')
    
# Event 2: Hallway with the Royal Guards - Use Charisma
delay_print('You move deeper into the castle, and soon find yourself face-to-face with two royal guards blocking a passage.')
delay_print('They look at you suspiciously, their weapons drawn. You need to convince them to let you pass.')
event = Event(player, 'medium', 'charisma')
print(f'1. Use your charisma to try to convince the guards to let you pass [{event.basic_success_chance}%] {colored(f"(+{event.define_succes_including_skills()}% DUE TO {event.required_skill.upper()} SKILLS)", color=event.COLORS[event.required_skill])}\n2. Draw your weapon and prepare for a fight')

royal_guards = safe_input('', [1, 2])

if royal_guards == 1:
    if event.take_a_try():
        delay_print('You speak calmly and confidently, and the guards are convinced that you are on official business. They step aside and let you pass.')
    else:
        delay_print('You try to bluff, but the guards are not fooled. They draw their weapons and prepare to fight!')
        combat = Combat(player, Enemy('Royal Guard', 5, 2, 2, 0, 50, False))
        combat.start_combat()
        if combat.is_lost:
            delay_print('The guards overpower you, and you are thrown into the dungeon where your fate is sealed.')
            delay_print('Game Over.')
            quit()

else:
    delay_print('You prepare to fight the guards, drawing your weapon.')
    combat = Combat(player, Enemy('Royal Guard', 5, 2, 2, 0, 50, False))
    combat.start_combat()
    if combat.is_lost:
        delay_print('The guards overpower you, and you are thrown into the dungeon where your fate is sealed.')
        delay_print('Game Over.')
        quit()

# Event 3: The Final Boss - Use Intelligence
delay_print('Finally, you reach the throne room. The air is thick with dark magic. Standing before you is a powerful sorcerer who has been causing the disappearances.')
delay_print('He turns and faces you, his eyes glowing with malice.')
event = Event(player, 'hard', 'intelligence')
print(f'1. Use your intelligence to try to decipher the ancient runes on the walls and weaken the sorcerer [{event.basic_success_chance}%] {colored(f"(+{event.define_succes_including_skills()}% DUE TO {event.required_skill.upper()} SKILLS)", color=event.COLORS[event.required_skill])}\n2. Rush forward and engage in combat')

final_battle = safe_input('', [1, 2])

if final_battle == 1:
    if event.take_a_try():
        delay_print('You quickly decipher the runes and cause a magical backlash that weakens the sorcerer. His power diminishes, making the fight much easier.')
        delay_print('You strike him down and bring peace to the land.')
        delay_print(colored('You have won!', 'green'))
    else:
        delay_print('You try to read the runes, but they are too complex. The sorcerer unleashes a powerful spell that overwhelms you.')
        delay_print(colored('You are dead!', 'light_red'))
else:
    delay_print('You charge toward the sorcerer, sword in hand, but he casts a spell that knocks you off your feet.')
    combat = Combat(player, Enemy('Dark Sorcerer', 8, 8, 8, 8, 100, True))
    combat.start_combat()
    if combat.is_lost:
        delay_print('The dark magic overwhelms you, and the last thing you hear is the laughter of the sorcerer as your life fades away.')
        delay_print('Game Over.')
    elif not combat.is_lost and not combat.win_by_negotiation:
        delay_print('With the sorcerer defeated, the curse on the land is lifted. You are hailed as a hero by the grateful villagers.')
        delay_print('The once-abandoned castle is now a place of peace and prosperity.')
        delay_print('Congratulations, you have saved your homeland!')
    elif not combat.is_lost and combat.win_by_negotiation:
        delay_print('You step forward, raising your hands in peace, your voice calm and steady.')
        delay_print('"I see now the true power you wield," you say. "This land is broken, ruled by weak kings and fools. I could help you reshape it... if you let me."')
        delay_print('The sorcerer pauses, eyeing you with suspicion. Then a dark smile spreads across his face.')
        delay_print('"You have a sharp mind," he says, "and ambition. I could use someone like you."')
        delay_print('Without hesitation, you lower your weapon and kneel before him, swearing your allegiance. The sorcerer nods approvingly.')
        
        delay_print('Together, you begin to weave a new order. The kingdom falls into darkness, with you as his right hand, wielding power and magic beyond imagination.')
        delay_print('The villagers, the peasants, and the royalty who once resisted you are all crushed beneath your new reign.')

        delay_print(colored('The world will know your name... as the one who joined the dark power and reshaped the fate of the land.', 'red'))