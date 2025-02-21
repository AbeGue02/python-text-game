# Abraham Guerrero

inventory = []

#This dictionary links a room to other rooms.
rooms = {
    'Entrance': {
        'move': {'north': 'Courtyard'},
        'items': [],
        'description': ''
    },
    'Courtyard': {
        'move': {'north': 'City Gate', 'south': 'Entrance'},
        'items': [],
        'description': ''
    },
    'City Gate': {
        'move': {'east': 'Hallway', 'west': 'Statue', 'north': 'City', 'south': 'Courtyard'},
        'items': [],
        'description': ''
    },
    'Statue': {
        'move': {'west': 'Cathedral', 'east': 'City Gate'},
        'items': [],
        'description': ''
    },
    'Cathedral': {
        'move': {'east': 'Statue'},
        'items': [],
        'description': ''
    },
    'Hallway': {
        'move': {'west': 'City Gate', 'east': 'Library'},
        'items': [],
        'description': ''
    },
    'Library': {
        'move': {'west': 'Hallway'},
        'items': [],
        'description': ''
    },
    'City': {
        'move': {'south': 'City Gate'},
        'items': [],
        'description': ''
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
    if command in current_room:
        current_room = rooms[current_room[command.lower()]]
    elif command == 'exit':
        current_room = command

# Gameplay Loop
while current_room != 'exit':
    print_available_movement()
    user_input = input().lower()

    if (user_input in current_room) or (user_input == 'exit'):
        move_rooms(user_input)
    else:
        print('Invalid. Please try again')
else:
    print("You have exited")





