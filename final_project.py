# Abraham Guerrero

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
        'description': 'This city is absolutely massive. It looks like no one has been here for centuries. What secrets will we find?\nWhat is that pile of bones there?'
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
        current_room = rooms[current_room['move'][command]]
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

def print_inventory():
    global inventory
    print(f'Inventory: {inventory}', end='\n\n')


def main():

    print(game_start_text)

    while current_room != 'exit':
        print_available_movement()
        user_input = input().lower()

        if (user_input in current_room['move']) or (user_input == 'exit'):
            move_rooms(user_input)
        elif user_input == 'i':
            inspect_room()
        elif user_input == 'inv':
            print_inventory()
        else:
            print('Invalid. Please try again')
    else:
        print("You have exited")


# Gameplay Loop
if __name__ == "__main__":
    main()  # Call the main function





