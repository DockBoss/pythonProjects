# This the first python projects of many
# This will be a simple text adventure game
# Titled: Space Walk
import re  # importing regular expressions
import random


def game_over():
    print('You died')


def win():
    print('you survived!')


# Simple fight simulator determines if a shot is a hit or miss and runs for each fighter one side at a time
def fight(fighters):
    hits = 0
    for i in range(fighters):
        if random.random() >= 0.6:
            hits += 1
    return hits


def scene_two_run():
    print('You follow the crowd running as fast as you can to the escape pods. Every other step checking over\n'
          'your shoulders with the fear that you will see a group of rebels each time you do.\n'
          'You get enter the exit bay and see crew scrambling to get into the escape pods.\n'
          'There are 4 pods left, people are waiting in line to load up. There are 20 people waiting to get in the\n'
          'pods. You breath a sigh of relief exactly enough pods for everyone.\n'
          'Before you finish the thought you hear gunfire in the distance.\n'
          'The crowd loses all order and devolves into chaos. The person ahead of you pushes through\n'
          'the crowd and launches the end pod without waiting for anyone.\n'
          'Three pods left for 19 people')
    choice = input('Do you "wait" and help load everyone up, "stay" and accept your fate, or "push" your way though\n'
                   'the crowd to ensure your safety at the cost of the others?\n')
    if re.match(r'stay', choice, flags=re.I):
        print('It doesn\'t take a genius to realize everyone is not going to make it. A chill runs through your whole\n'
              'body as know what needs to happen. You decide to take that fall. You never know your crew might\n'
              'save the day. You turn and start walking towards the gunfire ignoring the others telling you to get in\n'
              'the pod with them. As you get closer to the commotion the gun fire stops.\n'
              'Your heart swells with hope as you round the corner to see a band of pirates looting the\n'
              'bodies of your crew. You reach for your gun to defend yourself, but you are not quick enough.')
        game_over()
    elif re.match(r'wait', choice, flags=re.I):
        print('You wait patently as everyone files into the pods gun fire still ringing in the distance.\n'
              'You squeeze into the last pod and which definitely has more people that it was designed for\n'
              'You say a prayer and close the hatch.\n'
              'The pod shoots out and you are thrown to the wall and everything goes black.\n')
        win()
    else:
        print('Fuck em you need to survive, You shove the lady ahead of you down and sprint towards the pod.\n'
              'A hand grips your shoulders trying to pull you from the pod. You turn and shoot them in the chest\n'
              'before you even see who it is. Freed from their grasp you close and launch the hatch.\n'
              'Leaving the 17 people with some tough decisions to make.\n'
              'You don\'t dwell on it though, all you can think of is that you are glad to be alive')
        win()

def scene_two_fight():
    print('You grip your pistol tighter and run in the opposite direction of the crowd.\n'
          'You make it down a few hallways before you hear gun fire coming from the flight deck.\n'
          'The moment you enter the flight deck a laser just misses you, as you stumble into a battle.\n'
          'There are 12 pirates and 6 crew members in an intense fire fight. You see a number of your fellow crew\n'
          'members dead on the ground and the other 6 desperately fighting to save the ship.\n'
          'You hide behind a create and prepare to fight')
    pirates, crew = (12, 7)
    fighting, your_turn = (True, True)
    while fighting:
        if your_turn:
            input('continue...\n')
            pirates -= fight(crew)
            if pirates < 1:
                print('You killed all the pirates')
                fighting = False
                win()
            else:
                print('Your aim is on point. There is {0} pirates left'.format(pirates))
        else:
            crew -= fight(pirates)
            if crew < 1:
                print('You all died')
                fighting = False
                game_over()
            else:
                print('These pirates are good. There is {0} crew members left. You start to shake a bit'.format(crew))
        your_turn = not your_turn


def scene_one():
    scene = 'You awake suddenly with a jolt as sirens blare and red lights flash.\n' \
            'You hear over the speaker "Evacuate immediately the ship has been boarded!"\n'
    print(scene)
    choice = input('Do you "leave" or "stay"?\n')
    if re.match(r'stay', choice, flags=re.I):
        print('You assume it is just a drill and hit the mute button for the speaker and the room goes silent.\n'
              'You breath a sigh of reliefe as you lie back down in hopes to fall back asleep.\n'
              'Right as you feel yourself drifting off to sleep you hear the door to your room open.\n'
              'You roll over and the last thing you see is the barrel of a gun pointed right at your head.')
        game_over()
    else:
        print('You jump out of bed and quickly put on your uniform and grab your pistol.\n'
              'You brace yourself and open the door. The noises of panic start drift in the second you open the door.\n'
              'You see your crew mates looking as tired and confused as yourself while others are yelling and running\n'
              'in the direction of the escape pods.')
        choice2 = input('Do you "follow" the crowd towards the escape pods or do you "run" the other way?\n')
        if re.match(r'follow', choice2, flags=re.I):
            scene_two_run()
        else:
            scene_two_fight()


start = input('Would you like to play a game?\n')
if re.match(r'yes', start, flags=re.I):
    scene_one()
