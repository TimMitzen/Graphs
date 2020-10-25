from room import Room
from player import Player
from world import World
import time
import sys
import pprint

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
start_room=[]#starting value for the strting location
start_room.append(player.current_room.id)
visited_rooms = set()

while len(visited_rooms) != len(world.rooms):
    current_room = start_room[-1]# -1 is for the last item in start_room
    visited_rooms.add(current_room)
    cache = []
    next_room = room_graph[current_room][1]
    #print(next_room.values())#room next to the current room
    for rooms in next_room.values():
        if rooms not in visited_rooms:
            cache.append(rooms)
    if len(cache) > 0:
        start_room.append(cache[0])#if cache exist add to start_room
    else:
        start_room.pop()
    #print(next_room.items)
    for rooms in next_room.items():
        if rooms[1] == start_room[-1]:
            traversal_path.append(rooms[0])
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
