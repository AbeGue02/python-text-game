# Abraham Guerrero

#This dictionary links a room to other rooms.
rooms = {
    'Entrance': {'north': 'Courtyard'},
    'Courtyard': {'north': 'City Gate', 'south': 'Entrance'},
    'City Gate': {'east': 'Hallway', 'west': 'Statue', 'north': 'City', 'south': 'Courtyard'},
    'Statue': {'west': 'Cathedral', 'east': 'City Gate'},
    'Cathedral': {'east': 'Statue'},
    'Hallway': {'west': 'City Gate', 'east': 'Library'},
    'Library': {'west': 'Hallway'},
    'City': {'south': 'City Gate'},
}

#Starting room
current_room = rooms['Entrance']

# Function prints available movement options in a room
def print_available_movement():
    print('Type the direction in which you would like to go:')
    for move_option in current_room.keys():
        print(f'[{move_option.capitalize()}]: {current_room[move_option]}')
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





