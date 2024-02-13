import networkx as nx
import matplotlib.pyplot as plt
import os
import subprocess

from src.logger import logging



class FilePath():
    def __init__(self):
        self.root_dir = os.path.abspath(".")
        self.folder_name = "artifacts"
        self.file_name= "shortest_paths.dot"
        self.artifacts_dir = os.path.join(self.root_dir, self.folder_name)
        
    def root_path(self):
        try:
            if not os.path.exists(self.artifacts_dir):
                os.makedirs(self.artifacts_dir)
            file_path = os.path.join(self.artifacts_dir, self.file_name)
            return file_path
        
        except Exception as e:
            logging.error(e)
            raise e


class BuildDotFile():
    def __init__(self):
        self.file_path = FilePath()

    def build_dot_file(self, paths, start, end):
        """
        This function will write the dot file

        Args:
            path: takes the shortest paths which has been found
            start: starting points taken as input 
            end: ending points taken as input

        """


        try:
            with open(self.file_path.root_path(), "w") as f:
                f.write("digraph K {\n")
                for i, path in enumerate(paths):
                    for j in range(len(path) - 1):
                        f.write(f"\"{path[j]}\" -> \"{path[j+1]}\" [label=\"1 step\"];\n")
                f.write(f"\"{start}\" [label=\"{start}\"];\n")
                f.write(f"\"{end}\" [label=\"{end}\"];\n")
                f.write("}\n")

        except Exception as e:
            logging.error(e)
            raise e
        



class DisplayDotFile():

    def __init__(self):
        self.file_path = FilePath()

    def display_dot_file(self):
        """
        Display the content of a DOT file using networkx and Matplotlib.
        """
        G = nx.drawing.nx_agraph.read_dot(self.file_path.root_path())
        nx.draw(G, with_labels=True)
        plt.show()




def get_position():
    while True:
        try:
            position = input("Enter position (x y): ").strip().split()
            x, y = map(int, position)
            if 0 <= x <= 7 and 0 <= y <= 7:
                return (x, y)
            else:
                raise ValueError("Coordinates must be between 0 and 7.")
        except ValueError as e:                
            print(str(e))


def save_png():

    
    dot_file = "./artifacts/shortest_paths.dot"
    save_file = "./artifacts/shortest_png.png"

    result = subprocess.run(
        ["dot", "-Tpng", dot_file, "-o", save_file],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print("PNG file created successfully.")

