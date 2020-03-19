import random
from util import Queue

# helpers
def get_new_room(exits):
    new_room = {'n': None, 's': None, 'w': None, 'e': None}

    for direction in exits:
        new_room[direction] = '?'

    return new_room

def get_random_unexplored_direction(room_id, traversal_graph):
    exits = traversal_graph[room_id]
    unexplored_exits = []

    for direction in exits:
        if exits[direction] == '?':
            unexplored_exits.append(direction)
    
    if len(unexplored_exits) > 0:
        random_direction = unexplored_exits[random.randint(0, len(unexplored_exits) - 1)]
        return random_direction

def get_opposite_direction(direction):
    opposites = {
        'n': 's',
        'e': 'w',
        's': 'n',
        'w': 'e'
    }

    return opposites[direction]

def bf_backtrack(traversal_graph, current_room_id):
    # keep track of to_visit queue (of room ids)
    to_visit = Queue()
    to_visit.enqueue(current_room_id)
    # keep track of path/directions
    paths = Queue()
    paths.enqueue([])
    # keep track of visited
    visited = set()

    # while rooms in to_visit
    while to_visit.size() > 0:
        # dequeue to_visit
        current_room_id = to_visit.dequeue()

        # dequeue paths
        path = paths.dequeue()

        # if room hasn't been visited,
        if current_room_id not in visited:
            # if it's the target room (i.e. it has at least one unexplored exit)
            if current_room_id == None or get_random_unexplored_direction(current_room_id, traversal_graph) != None:
                # return path
                return path
            # else
            # add the room to visited
            visited.add(current_room_id)
            # loop over adjacent rooms and add them to to_visit
            for direction in traversal_graph[current_room_id]:
                if traversal_graph[current_room_id][direction] != None:
                    to_visit.enqueue(traversal_graph[current_room_id][direction])
                    paths.enqueue(path + [direction])