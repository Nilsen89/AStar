import sys

class AStar:
    def __init__(self):
        return 0
    


class Data: 
    
    tree = list()
    goal = [0,0]
    start = [0,0]

    def __init__(self):
        with open(sys.argv[1], 'r') as my_file:
            row = 0
            for word in my_file:
                temp_arr = list()
                col = 0
                for char in word:
                    temp_arr.append(Cell(row, col, char))
                    if char == 'A':
                        self.start[0] = row
                        self.start[1] = col
                    if char == 'B':
                        self.goal[0] = row
                        self.goal[1] = col
                    col += 1
                self.tree.append(temp_arr)
                row += 1

    def printTree(self):
        print("Start: " + str(self.start[0]) + "-" + str(self.start[1]))
        print("Goal: " + str(self.goal[0]) + "-" + str(self.goal[1]))
        for row in self.tree:
            for col in row:
                sys.stdout.write(col.char)
                sys.stdout.flush()

class Cell:
    x = 0 # row cord
    y = 0 # col cord
    h = 0 # approx. dist to goal
    wall = False # if cell is wall
    char = '' # displayed character

    def __init__(self,row, col, char):
        x = row
        y = col
        self.char = char
        if(char == '#'):
            wall = True

def main():
    data = Data()
    data.printTree()

main()
