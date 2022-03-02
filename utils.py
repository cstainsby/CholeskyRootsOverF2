import numpy as np

import simpleCholSqrtGenerator

def generate_upper_triangular_matrix_of_nxn(n):
    """
    DESC:                                                                                 \n
    create an upper triangular matrix with the upper triangle values as undetermined(-1)  \n
    this matrix can form any upper triangular matrix                                      \n
    PARAMS                                                                                \n
    n(int): specifies the length of the square matrix being generated                     \n
    """
    upper_tri_matrix = np.zeros((n, n), dtype="int16")

    for i in range(n):
        for j in range(n):
            if i <= j:
                upper_tri_matrix[i][j] = und
    return upper_tri_matrix

def contains_np_matrix(search_matrix, matrix_list):
    index_of_matrix_in_list  = None # will remain None until the matrix is found, return None otherwise

    for i, matrix in enumerate(matrix_list):
        if any(np.array_equal(search_matrix, matrix)):
            index_of_matrix_in_list = i
            print(str(matrix) + " is equal to " + str(search_matrix))

    return index_of_matrix_in_list


def pretty_print_list_of_matrices(list_of_matrices):
    for i, list in enumerate(list_of_matrices):
        simpleCholSqrtGenerator.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)
