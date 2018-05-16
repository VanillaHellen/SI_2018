import heapq

class PriorityQueue:
    def __init__(self, order='min', f=lambda x: x):
        self.heap = []

        if order == 'min':
            self.f = f
        elif order == 'max':  # now item with max f(x)
            self.f = lambda x: -f(x)  # will be popped first
        else:
            raise ValueError("order must be either 'min' or max'.")

    def append(self, item):
        heapq.heappush(self.heap, (self.f(item), item))

    def extend(self, items):
        for item in items:
            self.heap.append(item)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def __len__(self):
        return len(self.heap)

    def __contains__(self, item):
        return (self.f(item), item) in self.heap

    def __getitem__(self, key):
        for _, item in self.heap:
            if item == key:
                return item

    def __delitem__(self, key):
        self.heap.remove((self.f(key), key))
        heapq.heapify(self.heap)

########################################################################################################################

class Problem(object):

    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def path_cost(self, c, state1, action, state2):
        return c + 1


class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_node = problem.result(self.state, action)
        return Node(next_node, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_node))

    def reconstruct_path(self):
        return [node.action for node in self.path()[1:]]   # [1:] creates copy of list instead of overwriting it

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

########################################################################################################################


def best_first_graph_search(problem, f):
    explored = set()
    current = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(current)

    while frontier:
        current = frontier.pop()
        if problem.goal_test(current.state):
            return current
        explored.add(current.state)

        for child in current.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                current_path = frontier[child]
                if f(current_path) >= f(child):
                    del frontier[current_path]
                    frontier.append(child)

    return None


def astar_search(problem):
    heuristic = problem.heuristic

    return best_first_graph_search(problem, lambda n: n.path_cost + heuristic(n))

########################################################################################################################

class Plan_Route(Problem):

    def __init__(self, initial, goal, walls):

        Problem.__init__(self, initial, goal)
        self.walls = walls

        self.x_size = 20
        self.y_size = 20

    def actions(self, state):

        actions = ['right', 'left', 'up', 'down']
        x, y = state

        if x == 0:
            if 'left' in actions:
                actions.remove('left')
        if x == (self.x_size - 1):
            if 'right' in actions:
                actions.remove('right')
        if y == 0:
            if 'up' in actions:
                actions.remove('up')
        if y == (self.y_size - 1):
            if 'down' in actions:
                actions.remove('down')

        return actions

    def result(self, state, action):
        x,y = state
        proposed_loc = tuple()

        if action == 'up':
            proposed_loc = (x, y - 1)
        elif action == 'down':
            proposed_loc = (x, y + 1)
        elif action == 'left':
            proposed_loc = (x - 1, y)
        elif action == 'right':
            proposed_loc = (x + 1, y)
        else:
            raise Exception('InvalidAction')

        if proposed_loc in self.walls:
            state = proposed_loc

        return state


    def goal_test(self, state):
        return state == self.goal

    def heuristic(self, node):

        x1,y1 = node.state
        x2,y2 = self.goal

        return abs(x2 - x1) + abs(y2 - y1)
