import numpy as np

import utils

UNDEFINED = -1

class Node:
    # np array of the current node 
    current_arr = None

    # list of list of changes made to get to get to the children node
    # chanages will be stored as ((row, col) = value)
    operations = []

    # list of children Nodes
    # num children will scale 1:1 with GF
    children = []

def main():
    n = 2
    generate_tree(2, 2)


def generate_tree(GF, n):
    # max depth of the tree will be the sum of 1, ..., n
    max_depth = 1
    for i in range(0, n):
        max_depth += i

    general_upper_matrix = utils.generate_upper_triangular_matrix_of_nxn(n)
    root = Node()

    root.current_arr = np.array(general_upper_matrix)

    root = generate_tree_recurr(GF, n, root, 0)

    pretty_print_tree(root)

    return root

def generate_tree_recurr(GF, n, curr_node, curr_depth):
    col, row = depth_to_matrix_index_in_UT_terms(curr_depth)
    print()
    print("curr_depth: " + str(curr_depth))
    print("col: " + str(col) + " row: " + str(row))

    # base check
    # make sure tree generation stays within num undefined matrix positions 
    print("base check: col: " + str(col) + " n: " + str(n))
    if col >= n:
        return None

    curr_node.children = []
    curr_node.operations = []

    # for each of the "options" for a single unknown position (based on GF)
    for i in range(0, GF):
        # proposed child node
        # the recurrsive function will determine if it is valid, if so it will append it
        proposed_child = Node()
        proposed_child.current_arr = curr_node.current_arr
        proposed_child.current_arr[row][col] = i

        # the recurrsive function may return 
        returned_child = generate_tree_recurr(GF, n, proposed_child, curr_depth + 1)
        curr_node.children.append(returned_child)
        # curr_node.operations.append(((row,col), i))

    if returned_child is not None:
        if curr_node.children.count(None) == 0:
            # case 1: leaf node case
            # either originally a leaf node or an internal node that is now a leaf
            if utils.is_chol_matrix(GF, curr_node.current_arr):
                return curr_node
            else:
                return None
        elif curr_node.children.count(None) == 1:
            # if there is only one child, copy its contents into the current node
            curr_node.current_arr = returned_child.current_arr
            return curr_node
        else:
            # there are multiple children
            # 
            return curr_node
    else:
        return None


def pretty_print_tree(root):
    print()
    print("Printing tree ------------------")
    pretty_print_tree_recurr(root, 0)

def pretty_print_tree_recurr(curr_node, depth):
    print("print depth: " + str(depth))
    if curr_node is None:
        return
    
    print("depth: " + str(depth))
    print("operations:")
    for operation in curr_node.operations:
        print(operation)
    
    utils.pretty_print_numpy_array(curr_node.current_arr)

    for child_node in curr_node.children:
        pretty_print_tree_recurr(child_node, depth + 1)


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