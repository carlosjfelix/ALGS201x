# python3

import sys, threading
from pathlib import Path
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# creating class methods to calculate tree height
class TreeHeight:
        def read(self):
                """TreeHeight method to read a file and create tree"""
                # open directory where file is located and then read line by line
                folder = "C:/Users/cjfel/OneDrive/Desktop/Programming/Python/Data Structures Fundamentals/1_BasicDataStructures/Assignment1-2/tests/"
                textfile = folder + input("Input the name of the text file: ")
                f = open(textfile)

                # number of nodes n
                self.n = int(f.readline())
                
                # reads second line of text file that contains parents of nodes
                self.parent = list(map(int, f.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
