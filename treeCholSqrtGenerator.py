import copy
import numpy as np

import utils

und = -1

class Node:
    # np array of the current node 
    current_arr = None

    # list of list of changes made to get to get to the children node
    # chanages will be stored as ((row, col) = value)
    operations = None

    # list of children Nodes
    # num children will scale 1:1 with GF
    children = None

def main():
    n = 2
    generate_non_pruned_tree(2, 2)


def generate_non_pruned_tree(GF, n):
    # max depth of the tree will be the sum of 1, ..., n
    max_depth = 1
    for i in range(0, n):
        max_depth += i

    general_upper_matrix = utils.generate_upper_triangular_matrix_of_nxn(n)
    root = Node()

    root.current_arr = np.array(general_upper_matrix)

    generate_non_pruned_tree_recurr(GF, n, root, 0)

    pretty_print_tree(root)

def generate_non_pruned_tree_recurr(GF, n, curr_node, curr_depth):
    col, row = depth_to_matrix_index_in_UT_terms(curr_depth)
    print("curr_depth: " + str(curr_depth))
    print("col: " + str(col) + " row: " + str(row))

    # base check
    if col >= n:
        return None

    curr_node.children = []
    curr_node.operations = []

    for i in range(GF):
        new_child = Node()
        new_child.current_arr = curr_node.current_arr
        new_child.current_arr[col][row] = i

        generate_non_pruned_tree_recurr(GF, n, new_child, curr_depth + 1)
        curr_node.children.append(new_child)
        curr_node.operations.append(((row,col), i))



def prune_tree(check_function):
    pass

def pretty_print_tree(root):
    pretty_print_tree_recurr(root, 0)

def pretty_print_tree_recurr(curr_node, depth):
    if curr_node == None:
        return
    
    print("depth: " + str(depth))
    print("operations:")
    for operation in curr_node.operations:
        print(operation)
    
    utils.pretty_print_numpy_array(curr_node.current_arr)

    for child_node in curr_node.children:
        pretty_print_tree_recurr(child_node, depth + 1)


def find_changes():
    pass

def depth_to_matrix_index_in_UT_terms(curr_depth):
    # we will be itterating through the matrix starting at the top left, going col first
    #   [[a, b, d], [0, c, e], [0, 0, f]]    (in alphabetical order)
    # 
    row = curr_depth
    col = 0
    while row > col:
        row -= col + 1
        col += 1

    return col, row

if __name__ == "__main__":
    print("Starting treeCholSqrtGenerator main()")
    main()