class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    """'This is a class definition for a stack frontier"""
    """Used in depth first search"""
    def __init__(self):
        self.frontier = []

    def add(self, node):
        """Add a new node to the frontier"""
        self.frontier.append(node)

    def contains_state(self, state):
        """Check if a state is in the frontier"""
        return any(node.state == state for node in self.frontier)

    def empty(self):
        """Check if the frontier is empty"""
        return len(self.frontier) == 0

    def remove(self):
        """Remove and return the last node added to the frontier"""
        """This method raises an exception if the frontier is empty"""
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    """This is a class definition for a queue frontier"""
    """Inherits from StackFrontier"""
    """Used in breadth first search"""
    def remove(self):
        """Overriden Remove method"""
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
