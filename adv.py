from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

### Carnun:
def get_traversal_graph(room_graph, player) {
    # keep track of traversal_graph, starting in first room
    # keep track of a room stack, starting at first room
    # while there's a room in the stack
        # pop it
        # add it to traversal_path
        # if the room has unexplored exits, randomly pick one of them
            # move there
            # update traversal_graph (both exited and entered room!)
        # else, do a bfs to find shortest path to an unexplored room, and move there
            # call helper to get path
            # take path (and update traversal_path accordingly)
}

# helper
def bf_backtrack(traversal_graph, current_room):
    # keep track of to_visit queue (of paths)
    # keep track of visited
    # while rooms in to_visit
        # dequeue
        # if room hasn't been visited,
            # if it's the target room (i.e. it has at least one unexplored exit)
                # return path
            # else
                # add the room to visited
                # loop over adjacent rooms and add them to to_visit

###

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
