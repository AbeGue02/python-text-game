# Abraham Guerrero

inventory = []

#This dictionary links a room to other rooms.
rooms = {
    'Entrance': {
        'move': {'north': 'Courtyard'},
        'items': [],
        'description': 'This room is empty and there is debris on the floor. This place is really deteriorated.\nThe door which initially led us here is shut tight.'
    },
    'Courtyard': {
        'move': {'north': 'City Gate', 'south': 'Entrance'},
        'items': [],
        'description': 'This courtyard has a fountain in the middle. There seems to be sunlight coming through the ceiling somehow.\nMaybe people used to hang out here before?'
    },
    'City Gate': {
        'move': {'east': 'Hallway', 'west': 'Statue', 'north': 'City', 'south': 'Courtyard'},
        'items': [],
        'description': 'There is a large door here. There are two other hallways leading in different directions.\nLook! There seems to be a skeleton on the floor right in front of the door.'
    },
    'Statue': {
        'move': {'west': 'Cathedral', 'east': 'City Gate'},
        'items': [],
        'description': 'There is a statue of some ancient hero here.\nI wonder who they were and what they did.'
    },
    'Cathedral': {
        'move': {'east': 'Statue'},
        'items': [],
        'description': 'This is a large stone cathedral with lots of symbols we do not understand.\nMaybe these people worshipped a God we know naught about'
    },
    'Hallway': {
        'move': {'west': 'City Gate', 'east': 'Library'},
        'items': [],
        'description': 'There are empty suits of armor on both sides of this hallway.\nIt looks really creepy!'
    },
    'Library': {
        'move': {'west': 'Hallway'},
        'items': [],
        'description': 'This library has multiple floors. I can keep looking up and down but I see neither ceiling nor bottom floor.\nHow many books are there?'
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
    print('Type the direction in which you would like to go:')
    for move_option, destination in current_room['move'].items():
        print(f'[{move_option.capitalize()}]: {destination}')
    print('To end game, type "Exit"')

# This function handles the movement from one room to another
def move_rooms(command):
    global current_room
    if command in current_room['move']:
        current_room = rooms[current_room['move'][command]]
        print(current_room['description'])
    elif command == 'exit':
        current_room = command

# Gameplay Loop
while current_room != 'exit':
    print_available_movement()
    user_input = input().lower()

    if (user_input in current_room['move']) or (user_input == 'exit'):
        move_rooms(user_input)
    else:
        print('Invalid. Please try again')
else:
    print("You have exited")





