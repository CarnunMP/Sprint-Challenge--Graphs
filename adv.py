from room import Room
from player import Player
from world import World

from util import Stack
from helpers import get_new_room, get_random_unexplored_direction, get_opposite_direction, bf_backtrack

# import random
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
def traverse_graph(room_graph, player):
    # keep track of traversal_graph, starting in first room
    exits = player.current_room.get_exits()

    traversal_graph = {
        0: get_new_room(exits)
    }
    # keep track of a room stack, starting at first room
    to_visit = Stack()
    to_visit.push(0)

    # while there's a room in the stack
    while to_visit.size() > 0:
        # pop it
        current_room_id = to_visit.pop()
        # update traversal_path
        traversal_path.append(current_room_id)

        # if the room has unexplored exits, randomly pick one of them
        random_unexplored_direction = get_random_unexplored_direction(current_room_id, traversal_graph)
        if random_unexplored_direction != None:
            # move there
            player.travel(random_unexplored_direction)
            # update traversal_graph (both exited and entered room!)
            traversal_graph[player.current_room.id] = get_new_room(player.current_room.get_exits())
            traversal_graph[player.current_room.id][get_opposite_direction(random_unexplored_direction)] = current_room_id
            traversal_graph[current_room_id][random_unexplored_direction] = player.current_room.id

            to_visit.push(player.current_room.id)
        # else, do a bfs to find shortest path to an unexplored room, and move there
        else:
            # call helper to get path
            backtrack_path = bf_backtrack(traversal_graph, current_room_id)
            # take path (and update traversal_path accordingly)
            for direction in backtrack_path:
                player.travel(direction)
                traversal_path.append(direction)

            to_visit.push(player.current_room.id)


traverse_graph(room_graph, player)     


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
