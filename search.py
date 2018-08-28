# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
def depth_first_search(problem):
    visited_node = set()
    init_state = (problem.getStartState(), ['Stop'], 0)
    return visit_node(problem, init_state,visited_node)


def visit_node(problem,state, visited):
    current_node = state[0]
    if current_node in visited:
        return None
    current_path = state[1]
    current_cost = state[2]

    if problem.isGoalState(current_node):
        current_path.remove(current_path[0])
        return current_path
    visited.add(current_node)

    sub_states = problem.getSuccessors(current_node)
    if len(sub_states) is 0:
        return None

    for sub_state in sub_states:
        node = sub_state[0]
        action = sub_state[1]
        cost = sub_state[2]

        new_path = current_path + [action]
        new_cost = current_cost + cost

        new_state = (node, new_path, new_cost)
        path = visit_node(problem, new_state, visited)
        if path is not None:
            return path

def breath_first_search(problem, que, type = 'breath_first_search', heuristic = None):
    visited_node = set()
    init_state = (problem.getStartState(), ['Stop'], 0)
    if type is 'breath_first_search':
        que.push(init_state)
    elif type is 'uniformCostSearch':
        que.push(init_state, 0)
    elif type is 'aStarSearch':
        cost = init_state[2] + heuristic(init_state[0], problem)
        que.push(init_state, cost)

    while not que.isEmpty():
        curret_state = que.pop()
        if problem.isGoalState(curret_state[0]):
            curret_state[1].remove(curret_state[1][0])
            return curret_state[1]
        if curret_state[0] not in visited_node:
            visited_node.add(curret_state[0])
            for sub_state in problem.getSuccessors(curret_state[0]):
                node = sub_state[0]
                action = sub_state[1]
                cost = sub_state[2]

                new_path = curret_state[1] + [action]
                new_cost = curret_state[2] + cost

                new_state = (node, new_path, new_cost)
                if type is 'breath_first_search':
                    que.push(new_state)
                elif type is 'uniformCostSearch':
                    que.push(new_state, new_cost)
                elif type is 'aStarSearch':
                    cost = new_state[2] + heuristic(init_state[0], problem)
                    que.push(new_state, cost)

def search(problem, que, type):
    visited_node = set()
    init_state = (problem.getStartState(), ['Stop'], 0)
    if type is 'uniformCostSearch':
        cost = init_state[2]

def generic_search_1(problem, fringe, push_into_fringe):

    visited = set()
    # state model is (node, path, cost)
    start_state = (problem.getStartState(), ['Stop'], 0)
    push_into_fringe(fringe, start_state)

    if problem.isGoalState(problem.getStartState()):
        return 'Stop'

    while not fringe.isEmpty():
        current_state = fringe.pop()
        current_node = current_state[0]
        current_path = current_state[1]
        current_cost = current_state[2]

        if problem.isGoalState(current_node):
            current_path.remove(current_path[0])
            return current_path

        if current_node not in visited:
            visited.add(current_node)
            for successor in problem.getSuccessors(current_node):
                child_node = successor[0]
                child_action = successor[1]
                child_cost = successor[2]

                new_path = current_path + [child_action]
                new_cost = current_cost + child_cost

                new_state = (child_node, new_path, new_cost)
                push_into_fringe(fringe, new_state)


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    def push_into_fringe(fringe, state):
        fringe.push(state)

    return depth_first_search(problem)
    # return generic_search_1(problem, fringe, push_into_fringe)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return breath_first_search(problem, util.Queue())


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return breath_first_search(problem, util.PriorityQueue(), 'uniformCostSearch')
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    return breath_first_search(problem, util.PriorityQueue(), 'aStarSearch', heuristic)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
