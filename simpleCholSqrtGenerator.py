import numpy as np

import utils


# placeholder for an undetermined valu
UNDEFINED = -1


def main(output_location, GF, n):
    """
    DESC:
    driver for program
    """

    general_upper_matrix = utils.generate_upper_triangular_matrix_of_nxn(n)
    upper_triangular_list = find_matrix_list_from_gen(GF, general_upper_matrix)
    sqrt_list_at_n = generate_sqrt_matrices(GF, upper_triangular_list)
    chol_list_at_n = generate_chol_matrices(GF, upper_triangular_list)

    print("sqrt list")
    for matrix in sqrt_list_at_n:
        utils.pretty_print_numpy_array(matrix, with_index_labels=False, with_shape=False)

    print("\nchol list")
    for matrix in chol_list_at_n:
        utils.pretty_print_numpy_array(matrix, with_index_labels=False, with_shape=False)


def generate_sqrt_matrices(GF, matrix_list):
    """
    DESC:                                                                            \n
    given a list of matrices, find the ones that obey the type function              \n
    A matrix is a square root if a matrix M's (M * M) == zero matrix                 \n
    PARAMS                                                                           \n
    GF(int)                                                                          \n
    matrix_list(list of np matrices)                                                 \n
    INFO
    this can generate both chols and sqrts, just pass in the utils helper function to sort them out
    """
    type_matrix_list = []       

    for M in matrix_list:
        if utils.is_sqrt_matrix(GF, M):
            # the matrix will be classified as a sqrt matrix
            type_matrix_list.append(M)

    return type_matrix_list

def generate_chol_matrices(GF, matrix_list):
    """
    DESC:                                                                            \n
    given a list of matrices, find the ones that obey the type function              \n
    A matrix is a square root if a matrix M's (M * M) == zero matrix                 \n
    PARAMS                                                                           \n
    GF(int)                                                                          \n
    matrix_list(list of np matrices)                                                 \n
    INFO
    this can generate both chols and sqrts, just pass in the utils helper function to sort them out
    """
    type_matrix_list = []       

    for M in matrix_list:
        if utils.is_chol_matrix(GF, M):
            # the matrix will be classified as a sqrt matrix
            type_matrix_list.append(M)

    return type_matrix_list

def find_matrix_list_from_gen(GF, gen_matrix):
    """
    DESC:                                                                           \n
    base function for finding all permutations of a generalized matrix              \n
    PARAMS:
    flat_matrix: general matrix that has been flattened                             \n
    GF:          The field which our general matrix is allowed to span              \n
    """
    flat_gen_matrix = gen_matrix.flatten()

    result_list = recurr_create_matrix_permutations(flat_gen_matrix, GF, 0)

    # reshape result list back into original matrix
    for i in range(0, len(result_list)):
        result_list[i] = np.reshape(result_list[i], gen_matrix.shape)

    return result_list

def recurr_create_matrix_permutations(flat_matrix, GF, index):
    """
    DESC:                                                                           \n
    generate all possible matrix permutations given a flatend matrix with know and
    to be determined values                                                         \n
    PARAMS:             
    flat_matrix: general matrix that has been flattened                             \n
    GF:          The field which our general matrix is allowed to span              \n
    index:       The current index that is being split on currently                 \n
    """
    if index >= len(flat_matrix):
        # we have reached the end of the list, starting return process
        #   we will return an empty list
        return None
    
    if flat_matrix[index] >= 0:
        # when the value from the generalized matrix is greater than 0(not undefined)
        #   that will be the value at that position in all permutations of the result list
        output_perm_list = []
        
        result = recurr_create_matrix_permutations(flat_matrix, GF, index + 1)
        
        if result == None:
            output_perm_list.append(np.array([flat_matrix[index]], dtype="int16"))
        else: 
            for np_arr in result:
                output_perm_list.append(np.insert(np_arr, 0, flat_matrix[index], axis=0))
        return output_perm_list
    else:
        # otherwise the value is undefined and we will need to add more arrays for
        # the new permutations
        output_perm_list = []
        for i in range(0, GF):
            result = recurr_create_matrix_permutations(flat_matrix, GF, index + 1)
            if result == None:
                output_perm_list.append(np.array([i], dtype="int16"))
            else:
                for np_arr in result:
                    np_arr = np.insert(np_arr, 0, i, axis=0)
                    output_perm_list.append(np_arr)
        return output_perm_list


if __name__ == "__simpleCholSqrtGenerator__":
    GF = 0
    n = 0 
    
    GF = input("what do you want your GF to be(int): ")
    n = input("what do you want your n to be(int): ")
    main(None, GF, n)
