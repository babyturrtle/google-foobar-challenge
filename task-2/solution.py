def solution(src, dest):

    import numpy as np
    from collections import deque

    board = np.arange(64).reshape(8,8)  

    class Node:
        def __init__(self, x, y, dist=0):
            self.x = x
            self.y = y
            self.dist = dist
    
        def __hash__(self):
            return hash((self.x, self.y, self.dist))
    
        def __eq__(self, other):
            return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)


    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]


    srcXY = np.where(board == src)
    srcX = srcXY[0][0]
    srcY = srcXY[1][0]
    destXY = np.where(board == dest)
    destX =destXY[0][0]
    destY = destXY[1][0]
    source = Node(srcX, srcY)
    destination = Node(destX, destY)

    visited = set()
    q = deque()
    q.append(source)

    while q:
        node = q.popleft()
        x = node.x
        y = node.y
        dist = node.dist

        if x == destination.x and y == destination.y:
            return dist
        
        if node not in visited:
            visited.add(node)

            for i in range(8):
                x1 = x + row[i]
                y1 = y + col[i]

                if not (x < 0 or y < 0 or x >= 8 or y >= 8):
                    q.append(Node(x1, y1, dist + 1))