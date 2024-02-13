import heapq
from src.logger import logging


class KnightMove():

    def __init__(self):
        pass

        

    def knight_moves(self, position):
        """
        Generate all possible moves for the knight.
        """
        x, y = position
        moves = [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]
        return [move for move in moves if 0 <= move[0] < 8 and 0 <= move[1] < 8]
    
    def abs(self, position, end):
        """
        Calculate the heuristic value for a given position.
        """
        x1, y1 = position
        x2, y2 = end
        return abs(x1 - x2) + abs(y1 - y2)


    
    def shortest_paths(self, start, end):

        try:
            """
            Generate all shortest paths from a starting position to an ending position.
            """
            frontier = [(self.abs(start, end), 0, [start])]
            explored = set()
            paths = []
            min_cost = float('inf')
            while frontier:
                _, cost, path = heapq.heappop(frontier)
                position = path[-1]
                if position == end:
                    if cost < min_cost:
                        min_cost = cost
                        paths = [path]  # Start a new list of paths with the new minimum cost
                    elif cost == min_cost:
                        paths.append(path)  # Add this path to the list of paths with the minimum cost
                if position not in explored:
                    explored.add(position)
                    for move in self.knight_moves(position):
                        new_cost = cost + 1
                        new_path = path + [move]
                        heapq.heappush(frontier, (new_cost + self.abs(move, end), new_cost, new_path))

            if paths:
                logging.info("Shortest path has been found")
                print("\n Shortest path set with minimum move : \n")
                print(f"There are minimum {len(paths[0])} moves for the given positions")
                print("-----------------------------------------------------")
                for i, path in enumerate(paths):
                    print(f"Path {i+1}:")
                    print(path)
                print("-----------------------------------------------------")
    
            else:
                print("No paths found.")


            return paths
        
        except Exception as e:
            logging.error(e)
            raise e



