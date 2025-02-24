# Abraham Guerrero

# Intro text for the game
game_start_text = '''
After months of exploring an underground cave system infested with monstrosities and mysteries, 
four adventurers determined to find an ancient city rumored to contain the secrets of the universe 
seem to be in the last stretch of their trip. 

•	Garok: a sturdy warrior with armor that can protect him against almost any blow
•	Caspian: A well-studied priest the mission of keeping the rest of the adventurers blessed and safe from the dangers of the darkness
•	Arida: A royal sorceress who finds herself somehow called by this underground city, and one of the reasons why this mission was carried out
•	Ambrose: An adept explorer of these caves. They overheard the adventurers in danger and decided to stick along for their safety

The adventurers decided to rest one last time before entering a large gate with the name of the city 
written in an ancient language that Arida somehow finds herself able to speak. When they wake up and enter this gate, 
it closes behind them and they find themselves trapped behind it. Deep in the dungeon, 
the party can hear a very loud snoring sound that echoes on the walls. What dangers will they find? 
'''

# Starting inventory
inventory = []

#This dictionary links a room to other rooms.
rooms = {
    'Entrance': {
        'move': {'north': 'Courtyard'},
        'items': [],
        'description': 'This room is empty and there is debris on the floor. This place is really deteriorated.\nThe door which initially led us here is shut tight.',
    },
    'Courtyard': {
        'move': {'north': 'City Gate', 'south': 'Entrance'},
        'items': ['Holy Water'],
        'description': 'This courtyard has a fountain in the middle. There seems to be sunlight coming through the ceiling somehow.\nMaybe people used to hang out here before?',
        'inspect': 'The sunlight seems to be enchanted. You scoop some water in a flask from the fountain'
    },
    'City Gate': {
        'move': {'east': 'Hallway', 'west': 'Statue', 'north': 'City', 'south': 'Courtyard'},
        'items': ['Key A'],
        'description': 'There is a large door here. There are two other hallways leading in different directions.\nLook! There seems to be a skeleton on the floor right in front of the door.',
        'inspect': 'There is a skeleton under the debris. It seems to be holding a key.'
    },
    'Statue': {
        'move': {'west': 'Cathedral', 'east': 'City Gate'},
        'items': ['Ancient Sword'],
        'description': 'There is a statue of some ancient hero here.\nI wonder who they were and what they did.',
        'inspect': 'The sword the statue is holding seems to be real. Grok reaches up to grab it.'
    },
    'Cathedral': {
        'move': {'east': 'Statue'},
        'items': ['Key B'],
        'description': 'This is a large stone cathedral with lots of symbols we do not understand.\nMaybe these people worshipped a God we know naught about',
        'inspect': 'There seems to be something hidden behind the altar.'
    },
    'Hallway': {
        'move': {'west': 'City Gate', 'east': 'Library'},
        'items': ['Grimoire'],
        'description': 'There are empty suits of armor on both sides of this hallway.\nIt looks really creepy!',
        'inspect': 'Arida trips over something under the carpet. She lifts the carpet and sees something.'
    },
    'Library': {
        'move': {'west': 'Hallway'},
        'items': ['Key C'],
        'description': 'This library has multiple floors. I can keep looking up and down but I see neither ceiling nor bottom floor.\nHow many books are there?',
        'inspect': 'A desk has a drawer half open. You open it and see something shiny inside.'
    },
    'City': {
        'move': {'south': 'City Gate'},
        'items': [],
        'description': 'You unlock the door to the city using all three keys.\nThis city is absolutely massive. It looks like no one has been here for centuries. What secrets will we find?\nWhat is that pile of bones there?'
    },
}

#Starting room
current_room = rooms['Entrance']

# Function prints available movement options in a room
def print_available_movement():
    print('Where would you like to go?')
    for move_option, destination in current_room['move'].items():
        print(f'[{move_option.capitalize()}]: {destination}')
    print()
    print('[I] Inspect Room')
    print('[Inv] Check Inventory')
    print('[Exit] End Game')

# This function handles the movement from one room to another
def move_rooms(command):
    global current_room
    if command in current_room['move']:
        next_room_name = current_room['move'][command]
        next_room = rooms[next_room_name]

        # Check if player meets condition to enter the city
        if next_room_name == 'City':
            if 'Key A' in inventory and 'Key B' in inventory and 'Key C' in inventory:
                current_room = next_room
                print(current_room['description'])
            else:
                print("You seem to need three keys to enter the City.")
        else:  # For all other rooms, movement is normal
            current_room = next_room
            print(current_room['description'])
    elif command == 'exit':
        current_room = command

# Allows player to learn more info and grab items
def inspect_room():
    global current_room
    if current_room['items']:
        print(current_room['inspect'])
        print(f'The party obtains {current_room["items"][0]}.')
        inventory.append(current_room["items"].pop(0))
    else:
        print('Nothing to see here.')
    print()

# prints player inventory
def print_inventory():
    global inventory
    print(f'Inventory: {inventory}', end='\n\n')

# Boss sequence to be played when the player enters the city
def boss_fight_sequence():
    boss_health = 3
    print('''
    The pile of bones in the middle of the city starts moving. Suddenly, a skeleton of a dragon reanimates.
    The party is taken aback, but they get ready for the fight that is ahead. The dragon looks at them
    and speaks to them in a language that they do not understand... except Arida, who somehow manages to.
    
    "If you seek to steal the knowledge in this city, you will first have to defeat me. I am the guardian of
    the secrets of the city, and I will not let you have them without a fight."
    ''')

    # Checks key items from inventory to use in boss battle
    if 'Holy Water' in inventory:
        print('Caspian spills the holy water on the dragon, making its undead skeleton burn with holy light', end='\n\n')
        boss_health -= 1
    if 'Ancient Sword' in inventory:
        print('Grok savagely slashes at the skeleton dragon with the ancient sword, and breaks some of its bones', end='\n\n')
        boss_health -= 1
    if 'Grimoire' in inventory:
        print('Arida reads an ancient spell from the grimoire she took and seals the dragon under magical chains', end='\n\n')
        boss_health -= 1

    # If all three items were used, they win
    if boss_health <= 0:
        print("The party manages to defeat the dragon. It becomes a pile of dust on the floor.")
        print("YOU WIN", end='\n')
        print('''
    The party moves on to the city and they find all sorts of secrets.
    Arida finds out about her draconic heritage, Grok finds the secret to becoming all powerful,
    Caspian finds out how the Gods became who they are today...
    
    But Ambrose? They watched. They gathered information, and left silently. Nobody has seen them since.''')
    # Otherwise, player loses
    else:
        print("The dragon manages to breath out some dark smoke on the party that drains them from their energy.")
        print("YOU LOSE", end='\n')
        print('''
    After some time, the party rises back from the ground. They are not the same. They cannot utter a word, and
    their bodies are weaker than ever. Somehow, they are still conscious, but lack control over their bodies.
    There is a craving for flesh that consumes them. They have now become servants of the guardian.''')

# Main Function
def main():

    print(game_start_text)

    # Runs game if not exit
    while current_room != 'exit':
        print_available_movement()
        user_input = input().lower()

        # Move if valid option
        if (user_input in current_room['move']) or (user_input == 'exit'):
            move_rooms(user_input)

            # If user moves to city, play boss fight sequence
            if current_room == rooms['City']:  # Check if player is in the city
                boss_fight_sequence()
                break
        # If user presses I, inspect room
        elif user_input == 'i':
            inspect_room()
        # If user types inv, check inventory
        elif user_input == 'inv':
            print_inventory()
        # Anything else is invalid
        else:
            print('Invalid. Please try again')
    else:
        print("You have exited")


# Gameplay Loop
if __name__ == "__main__":
    main()  # Call the main function





