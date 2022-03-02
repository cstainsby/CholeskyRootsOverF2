import numpy as np

import main

def contains_np_matrix(search_matrix, matrix_list):
    index_of_matrix_in_list  = None # will remain None until the matrix is found, return None otherwise

    for i, matrix in enumerate(matrix_list):
        if any(np.array_equal(search_matrix, matrix)):
            index_of_matrix_in_list = i
            print(str(matrix) + " is equal to " + str(search_matrix))

    return index_of_matrix_in_list


def pretty_print_list_of_matrices(list_of_matrices):
    for i, list in enumerate(list_of_matrices):
        main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)
