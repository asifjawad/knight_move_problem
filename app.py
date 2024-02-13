from src.shortest_path import KnightMove
from src.utils import BuildDotFile, get_position, DisplayDotFile, save_png
from src.logger import logging




def main():
    while True:
        start = get_position()
        end = get_position()    

        knight=KnightMove()
        logging.info("shortest path algorithm has started")
        short_paths = knight.shortest_paths(start, end)

        build_dot_file=BuildDotFile()

        build_dot_file.build_dot_file(short_paths, start, end)
        logging.info("Dot file has been created successfuly")

        print("dot file has been build to 'artifacts folder as shortest_paths.dot'")
        save = input("Do you want to save file in PNG (y/n) ").lower() == 'y'
        if save:
            save_png()

        display_graph = DisplayDotFile()
        display_graph.display_dot_file()

        restart = input("Do you want to find other shortest knight's move (y/n) ").lower() == 'y'
        if not restart:
            break

    



if __name__ == "__main__":

    print("------------------------------------------------")
    print("|   Shortest Path finder for Knight's Move     |")
    print("------------------------------------------------")
    print("|            Created by: Jawad Asif            |")
    print("------------------------------------------------")
    logging.info("- Application to find Knight's shortest move has started")
    print("- Enter Values between 0-7. You will be asked to Enter Starting and Ending Position.")
    print("- You need to Enter two single digit with one space e.g Enter Postion : (3 1)\n")

    main()




    


