import numpy as np
from copy import deepcopy
import sys

import utils

UNDEFINED = -1


class Node:
    """ 
    DESC:
        A Node in a tree used for generating paths from a generic upper-triangular matrix to each allowable matrix given a rule

    ATTRIBUTES:
        - current_arr(list of list of int): the matrix bound to the current Node
        - operations(tuple of tuple and int): parallel to children, operations used to get to each child
        - children(list of Nodes): parallel to operations, list of all Nodes reachable from the current Node

    METHODS: 
        None
    """
    # np array of the current node 
    current_arr = None

    # list of list of changes made to get to get to the children node
    # chanages will be stored as ((row, col) = value)
    operations = []

    # list of children Nodes
    # num children will scale 1:1 with GF
    children = []

class UT_Matrix_Tree():
    """
    DESC:
        An upper triangular matrix tree 

    ATTRIBUTES:
        - GF(int)
        - n(int)
        - root(Node): root of the tree
        - definition_function(func): function used to shape tree(sqrt/chol)

    METHODS: 
        None
    """
    root = None

    def __init__(self, definition_function, GF = 0, n = 0) -> None:
        """Constructor"""
        self.GF = GF
        self.n = n
        self.definition_function = definition_function

        self.DFS_generate_tree()
    # ---------------------------------------------------------------------------------
    #       construction helper functions
    # ---------------------------------------------------------------------------------
    def DFS_generate_tree(self):
        """
        DESC: 
            Initial call for the DFS generation of the matrix tree.
            The root node will always start as a generic upper triangular matrix

        PARAMS:
            N/A

        RETURN:
            - root(Node): The root node of the tree
        """
        general_upper_matrix = utils.generate_upper_triangular_matrix_of_nxn(self.n)
        self.root = Node()

        self.root.current_arr = np.array(general_upper_matrix, dtype="int16")
        self.root = self.DFS_generate_tree_recurr(self.root, 0)

    def DFS_generate_tree_recurr(self, curr_node, curr_depth):
        """
        DESC: 
            DFS recurrsive function used to generate the tree
            It will start by recurrsivly generating every possible child regardless of the chol/sqrt restriction in DFS 
            fashion until a leaf node is reached. At which point it will be caught by a base check to confirm that it is a leaf 
            node and assign it a list of children which are None. When backtracking, a series of checks based on the number of 
            None children will be made to determine if the tree can be condensed. 

        PARAMS:
            - GF(int): feild the matrix will be over
            - n(int): the side length of the square matrix
            - curr_node(Node): the current Node being operated on
            - curr_depth(int): the current depth of the curr_node

        RETURN:
            curr_node if the node should be in the final tree based off chol/sqrt specifications
            None otherwise
        """
        col, row = self.depth_to_matrix_index_in_UT_terms(curr_depth)

        # base check
        # make sure tree generation stays within num undefined matrix positions
        if col >= self.n:
            if self.definition_function(self.GF, curr_node.current_arr):
                curr_node.children = [None] * self.GF # must return a list of Nones for each potential child the node could have had given it was internal
                return curr_node
            else:
                return None

        curr_node.children = []
        curr_node.operations = []

        # for each of the "options" for a single unknown position (based on GF)
        for i in range(0, self.GF):
            # proposed child node
            # the recurrsive function will determine if it is valid, if so it will append it
            proposed_child = Node()
            proposed_child.current_arr = deepcopy(curr_node.current_arr)
            proposed_child.current_arr[row][col] = i

            # the recurrsive function may return 
            curr_node.children.append(self.DFS_generate_tree_recurr(proposed_child, curr_depth + 1))
            curr_node.operations.append(((row, col), i))

        children_list_size = len(curr_node.children)
        num_non_none_children = children_list_size - curr_node.children.count(None)

        # remove the operation that leads to each of the None children
        for i in range(len(curr_node.children) - 1, 0, -1):
            if curr_node.children[i] is None:
                curr_node.operations.pop(i)

        # backtrack checks for intermediate nodes to reduce tree to only paths that fit the chol/sqrt parameter
        if num_non_none_children == 0:
            # case 1: No valid children
            #   return None
            return None
        elif num_non_none_children == 1:
            # case 2: single child
            #   copy child contents into current node

            # find non-None child
            non_none_child_index = 0
            while curr_node.children[non_none_child_index] is None:
                non_none_child_index += 1

            # for operation in curr_node.children[non_none_child_index].operations:
            #     curr_node.operations.append(operation)
            
            curr_node.current_arr = deepcopy(curr_node.children[non_none_child_index].current_arr)
            curr_node.children = deepcopy(curr_node.children[non_none_child_index].children)

            return curr_node
        # case 3: Multiple non-None children
        #   do nothing
        return curr_node

    # ---------------------------------------------------------------------------------
    #       Tree utility functions
    # ---------------------------------------------------------------------------------
    def pretty_print_tree(self, with_children=True):
        """
        DESC: 
            Initial call for the DFS printing of the matrix tree.

        PARAMS:
            - root(Node): the root node of the tree

        RETURN:
            N/A
        """
        print()
        print("-----------------------------------------")
        print("     Printing tree ")
        print("-----------------------------------------")
        self.pretty_print_tree_recurr(self.root, 0, with_children)

    def pretty_print_tree_recurr(self, curr_node, depth, with_children):
        """
        DESC: 
            Recurrsive DFS function for printing the tree

        PARAMS:
            - curr_node(Node): the current node in the tree 
            - depth(int): the current depth in the tree

        RETURN:
            N/A
        """
        if curr_node is None:
            return
        
        print("Depth: " + str(depth))
        if depth == 0:
            print("ROOT")
        # print("operations:")
        # for operation in curr_node.operations:
        #     # each operation in form -> ((row, col), value)
        #     print(self.row_and_col_to_ascii_char(operation[0][0], operation[0][1]) + " set to " + str(operation[1]))
        
        utils.pretty_print_numpy_array(curr_node.current_arr, array_label="current matrix", with_index_labels=True, with_shape=True)

        if with_children:
            print("number of children: " + str(len(curr_node.children) - curr_node.children.count(None)))
            for i, child_matrix in enumerate(curr_node.children):
                # print children
                if child_matrix is None:
                    utils.pretty_print_numpy_array(None, array_label="child " + str(i), indent=4)
                else:
                    utils.pretty_print_numpy_array(child_matrix.current_arr, array_label="child " + str(i), indent=4)

        for child_node in curr_node.children:
            self.pretty_print_tree_recurr(child_node, depth + 1, with_children)



    # ---------------------------------------------------------------------------------
    #     Helper functions 
    # ---------------------------------------------------------------------------------
    def depth_to_matrix_index_in_UT_terms(self, curr_depth):
        """
        DESC: 
            Converts depth into a 2d matrix position to find index based on current depth
            Specifically limited to upper triangular postions

        PARAMS:
            - curr_depth(int): the current depth

        RETURN:
            - col(int): column
            - row(int): row
        """
        # we will be itterating through the matrix starting at the top left, going col first
        #   [[a, b, d], [0, c, e], [0, 0, f]]    (in alphabetical order)
        # 
        row = curr_depth
        col = 0
        while row > col:
            row -= col + 1
            col += 1

        return col, row

    def row_and_col_to_ascii_char(self, row, col):
        """
        DESC: 
            Used for operation generation
            based on row and column of the upper triangular matrix, generate the equivalent letter position
            e.g. n = 3 
            [[A, B, D],
            [0, C, E],
            [0, 0, F]]

        PARAMS:
            - row(int): row
            - col(int): col

        RETURN:
            - letter(char): A-Z
        """
        col_total = 0
        for i in range(col):
            col_total += i + 1

        return chr(row + col_total + 65)

    

def main():
    """Driver for program
    Command to run: python treeCholSqrtGenerator.py runtype GF n
    runtype = either "chol" or "sqrt"
    GF = any integer >= 0
    n = any integer >= 0"""
    runtype = sys.argv[1]
    GF = int(sys.argv[2])
    n = int(sys.argv[3])
    
    print("you entered \nruntype: " + runtype + "\nGF: " + str(GF) + "\nn: " + str(n))

    if len(sys.argv) != 4:
        print("error, incorrect amount of inputs")
        return
    if type(GF) is not int or GF < 0:
        print("error, GF is wrong")
        return
    if type(n) is not int or n < 0:
        print("error, n is wrong")
        return
    

    if runtype == "chol":
        tree = UT_Matrix_Tree(definition_function=utils.is_chol_matrix, GF=GF, n=n)
    elif runtype == "sqrt":
        tree = UT_Matrix_Tree(definition_function=utils.is_sqrt_matrix, GF=GF, n=n)
    else:
        print("error, unreadable runtype")
        return
    
    tree.DFS_generate_tree()
    tree.pretty_print_tree(with_children=True)




if __name__ == "__main__":
    print("Starting treeCholSqrtGenerator main()")
    main()