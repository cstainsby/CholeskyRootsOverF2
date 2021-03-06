import numpy as np

UNDEFINED = -1

def generate_upper_triangular_matrix_of_nxn(n):
    """
    DESC:                                                                                 
    create an upper triangular matrix with the upper triangle values as undetermined(-1)  
    this matrix can form any upper triangular matrix                                      

    PARAMS                                                                                
    n(int): specifies the length of the square matrix being generated                     
    
    """
    upper_tri_matrix = np.zeros((n, n), dtype="int16")

    for i in range(n):
        for j in range(n):
            if i <= j:
                upper_tri_matrix[i][j] = UNDEFINED
    return upper_tri_matrix

def contains_np_matrix(search_matrix, matrix_list):
    """search function for a matrix in list of matrices"""
    index_of_matrix_in_list  = None # will remain None until the matrix is found, return None otherwise

    for i, matrix in enumerate(matrix_list):
        if any(np.array_equal(search_matrix, matrix)):
            index_of_matrix_in_list = i
            print(str(matrix) + " is equal to " + str(search_matrix))

    return index_of_matrix_in_list


def pretty_print_list_of_matrices(list_of_matrices):
    for i, list in enumerate(list_of_matrices):
        pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)


def is_sqrt_matrix(GF, M):
    """Utility func for checking if a matrix is a sqrt"""
    return np.array_equal(mod_to_finite_field(GF, np.matmul(M, M)), np.zeros(M.shape, dtype="int16"))


def is_chol_matrix(GF, M):
    """Utility func for checking if a matrix is a chol"""
    return np.array_equal(mod_to_finite_field(GF, np.transpose(M).dot(M)), np.zeros(M.shape, dtype="int16"))

def mod_to_finite_field(GF, matrix):
        """                                                                       
        this function will be called after every operation to make sure         \n
        the output stays within the defined GF                                  \n
        """
        rows, cols = matrix.shape
        result = np.zeros(matrix.shape, dtype="int16")
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrix[i][j] % GF

        return result


def pretty_print_numpy_array(np_array, array_label = "", with_index_labels = False, with_shape = False, indent=0):
    """
    DESC:                                                                           \n
    creates a detailed print of a numpy array including its shape and a given title \n
    PARAMS:
    np_array(np.array):         the array that will be pretty printed               \n
    array_label(string):        the label to be displayed with the array            \n
    with_index_labels(boolean): choose whether you want your axis labeled           \n
    with_shape(boolean):        choose whether you want the shape displayed         \n
    """
    indent_str = " " * indent

    if array_label != "":
        print(indent_str + "<----" + array_label + "---->")
    else:
        print(indent_str + "<--------->")

    if np_array is None:
        # output None message and return early
        print(indent_str + " NULL")
        if array_label != "":
            print(indent_str + "<----" + ('-' * len(array_label))  + "---->")
        else:
            print(indent_str + "<--------->")
        print()
    else:
        rows, cols = np_array.shape
        if with_shape:
            print("Rows: " + str(rows))
            print("Cols: " + str(cols))

        if with_index_labels:
            print(indent_str + "  ", end="")
            for i in range(cols):
                print("|" + str(i) + " ", end="")
            print()

        print(indent_str, end="")
        for n in range((3 * cols) + 3):
            print("-", end="")
        print()

        for i, row in enumerate(np_array):
            if with_index_labels:
                print(indent_str + str(i) + " ", end="")

            print(indent_str, end="")
            for j, value in enumerate(row):
                if value == -1:
                    print("|und", end="")
                else:
                    print("|" + str(value) + " ", end="")

            print()
            print(indent_str, end="")
            for n in range((3 * cols) + 3):
                print("-", end="")
            print()

        if array_label != "":
            print(indent_str + "<----" + ('-' * len(array_label))  + "---->")
        else:
            print(indent_str + "<--------->")
        print()