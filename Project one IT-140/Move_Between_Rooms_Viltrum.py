"""Module Six Milestone: simplified movement prototype for the Viltrum text game."""

# A dictionary for the Viltrum text game.
# Each room links to the rooms the player can reach, keyed by direction.
rooms = {
    "Main Hub": {
        "north": "Science Laboratory",
        "south": "Medical Bay",
        "east": "Weapon Room",
        "west": "Crew Quarters",
    },
    "Science Laboratory": {"south": "Main Hub", "east": "Observation Tower"},
    "Observation Tower": {"west": "Science Laboratory"},
    "Crew Quarters": {"east": "Main Hub"},
    "Medical Bay": {"north": "Main Hub", "east": "Maintenance Room"},
    "Maintenance Room": {"west": "Medical Bay"},
    "Weapon Room": {"west": "Main Hub", "north": "Throne Room"},
    "Throne Room": {"south": "Weapon Room"},
}

# The item sitting in each room (None = no item, or already collected).
room_items = {
    "Main Hub": None,
    "Science Laboratory": "Data Stick",
    "Observation Tower": "Navigation Map",
    "Crew Quarters": "Keycard",
    "Medical Bay": "Bandage",
    "Maintenance Room": "Battery Cell",
    "Weapon Room": "GreatSword",
    "Throne Room": None,
}

# Items the player has collected so far.
inventory = []

# Divider line printed around the room description.
DIVIDER = "-" * 51

# The player starts in the Main Hub.
current_room = "Main Hub"

print("Welcome to Viltrum! Kregg has taken over the station.")
print("Commands: go north, go south, go east, go west, get <item>, or exit.")

# Gameplay loop: runs until the player's room is set to "exit".
while current_room != "exit":
    # 1. Display the current room and the directions available from it.
    print("\n" + DIVIDER + "\n")
    if current_room == "Main Hub":
        print(f"You are in the {current_room} aka Start Point.")
    else:
        print(f"You are in the {current_room}.")
    print("\n" + DIVIDER + "\n")
    print("Inventory :", ", ".join(inventory) if inventory else "Empty")
    print("Item :", room_items[current_room] or "None")
    print("Direction :", ", ".join(rooms[current_room]))

    # 2. Prompt for a command (lowercased, extra spaces removed).
    command = input("Enter Your Move : ").strip().lower()

    # 3. Branch on the command.
    if command == "exit":
        # Exit command: set the room to "exit" so the loop ends.
        print("Thanks for playing!")
        current_room = "exit"
    elif command.startswith("go "):
        # Everything after "go " is the direction.
        direction = command[3:].strip()

        if direction in rooms[current_room]:
            # 4. Valid move: update the room using the dictionary.
            current_room = rooms[current_room][direction]
            print(f"You move {direction} into the {current_room}.")

            # Ending check from the Project One pseudocode:
            # entering the villain room ends the prototype.
            if current_room == "Throne Room":
                print("You have encountered Kregg!")
                current_room = "exit"
        else:
            # Direction is not linked to this room.
            print("You can't go that way. Try a different direction.")
    elif command.startswith("get "):
        # Everything after "get " is the requested item.
        requested_item = command[4:].strip()
        room_item = room_items[current_room]

        if room_item is not None and requested_item == room_item.lower():
            # Valid request: add to inventory and clear the room's item.
            inventory.append(room_item)
            room_items[current_room] = None
            print(f"You picked up the {room_item}.")
        else:
            # Item is not here; the inventory does not change.
            print(f"There is no {requested_item} in this room.")
    else:
        # Anything else is an invalid command.
        print("Invalid command. Use 'go <direction>', 'get <item>', or 'exit'.")

# 5. The loop has ended.
print("\nGame over.")