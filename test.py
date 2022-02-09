import main
import numpy as np 
import pytest

und = -1
GF = 2

# def test_one_by_one_matrix():
#     """ test the one by one upper triangluar matrix 
#     test generation of all cholesky roots of 1x1
#     """
#     # general matrix
#     upper_triangular_general_matrix_1x1 = np.array([und], dtype="int16")

#     # list that spans all possibilities from general matrix
#     upper_triangular_list_1x1 = main.find_matrix_list_from_gen(GF, upper_triangular_general_matrix_1x1)

#     print("generated lists")
#     for i, list in enumerate(upper_triangular_list_1x1):
#         main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)

#     cholesky_list = main.generate_cholesky_roots_matrices(GF, upper_triangular_list_1x1)

#     # all cholesky roots of 1 x 1
#     test_list = [np.array([[0]])]

#     print("test list")
#     for i, list in enumerate(test_list):
#         main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)

#     compare_test_and_result_lists_utility(result_list=cholesky_list, test_list=test_list)

                

def test_two_by_two_matrix_cholesky():
    """test the two by two upper trianglar matrix 
    test generation of all cholesky roots of 2x2
    """
    # general matrix
    upper_triangular_general_matrix_2x2 = main.generate_upper_triangular_matrix_of_nxn(2)

    # list that spans all possibilities from general matrix
    upper_triangular_list_2x2 = main.find_matrix_list_from_gen(GF, upper_triangular_general_matrix_2x2)

    print("generated lists")
    for i, list in enumerate(upper_triangular_list_2x2):
        main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)

    cholesky_list = main.generate_cholesky_roots_matrices(GF, upper_triangular_list_2x2)


    test_list = [np.array([[0, 0], [0, 0]]),
                np.array([[0, 1], [0, 1]])]

    print("test list")
    for i, list in enumerate(test_list):
        main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)

    compare_test_and_result_lists_utility(result_list=cholesky_list, test_list=test_list)

def test_three_by_three_matrix_cholesky():
    """test the three by three upper triangular matrix 
    test generation of all cholesky roots of 3x3
    """
    # general matrix 
    upper_triangular_general_matrix_3x3 = main.generate_upper_triangular_matrix_of_nxn(3)

    # list that spans all possibilities from general matrix
    upper_triangular_list_3x3 = main.find_matrix_list_from_gen(GF, upper_triangular_general_matrix_3x3)

    print("generated lists")
    for i, list in enumerate(upper_triangular_list_3x3):
        main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)

    cholesky_list = main.generate_cholesky_roots_matrices(GF, upper_triangular_list_3x3)


    test_list = [np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
                np.array([[0, 0, 0], [0, 0, 1], [0, 0, 1]]),
                np.array([[0, 0, 1], [0, 0, 0], [0, 0, 1]]),
                np.array([[0, 0, 1], [0, 0, 1], [0, 0, 0]]),
                np.array([[0, 1, 0], [0, 1, 0], [0, 0, 0]]),
                np.array([[0, 1, 1], [0, 1, 1], [0, 0, 0]])]
    
    print("test list")
    for i, list in enumerate(test_list):
        main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)

    compare_test_and_result_lists_utility(result_list=cholesky_list, test_list=test_list)


def test_two_by_two_matrix_sqrt():
    """test the two by two upper trianglar matrix 
    test generation of all sqrt of 2x2
    """
    # general matrix
    upper_triangular_general_matrix_2x2 = main.generate_upper_triangular_matrix_of_nxn(2)

    # list that spans all possibilities from general matrix
    upper_triangular_list_2x2 = main.find_matrix_list_from_gen(GF, upper_triangular_general_matrix_2x2)

    print("generated lists")
    for i, list in enumerate(upper_triangular_list_2x2):
        main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)

    sqrt_list = main.generate_square_root_matrices(GF, upper_triangular_list_2x2)


    test_list = [np.array([[0, 0], [0, 0]]),
                np.array([[0, 1], [0, 0]])]

    print("test list")
    for i, list in enumerate(test_list):
        main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)

    compare_test_and_result_lists_utility(result_list=sqrt_list, test_list=test_list)

def test_three_by_three_sqrt():
    """test the three by three upper triangular matrix 
    test generation of all sqrt of 3x3
    """
    # general matrix 
    upper_triangular_general_matrix_3x3 = main.generate_upper_triangular_matrix_of_nxn(3)

    # list that spans all possibilities from general matrix
    upper_triangular_list_3x3 = main.find_matrix_list_from_gen(GF, upper_triangular_general_matrix_3x3)

    print("generated lists")
    for i, list in enumerate(upper_triangular_list_3x3):
        main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)

    sqrt_list = main.generate_square_root_matrices(GF, upper_triangular_list_3x3)


    test_list = [np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
                np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]]),
                np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]]),
                np.array([[0, 0, 1], [0, 0, 1], [0, 0, 0]]),
                np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]]),
                np.array([[0, 1, 1], [0, 0, 0], [0, 0, 0]])]
    
    print("test list")
    for i, list in enumerate(test_list):
        main.pretty_print_numpy_array(list, "list #" + str(i + 1), with_index_labels= False, with_shape=False)

    compare_test_and_result_lists_utility(result_list=sqrt_list, test_list=test_list)

def compare_test_and_result_lists_utility(result_list, test_list):
    assert len(result_list) == len(test_list)

    # test shape of each array in chol list
    for i, array in enumerate(result_list):
        expected_rows, expected_cols = test_list[0].shape
        print(array.shape)
        actual_rows, actual_cols = array.shape
        assert expected_rows == actual_rows
        assert expected_cols == actual_cols

    for root in result_list:
        assert any(np.array_equal(test, root) for test in test_list)



def test_rule_upto_n():
    pass