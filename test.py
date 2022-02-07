import main
import numpy as np 
import pytest

und = -1
GF = 2

def one_by_one_matrix_test():
    """ test the one by one upper triangluar matrix 
    test generation of all cholesky roots of 1x1
    """
    # general matrix
    upper_triangular_general_matrix_1x1 = np.array([und], dtype="int16")

    # list that spans all possibilities from general matrix
    upper_triangular_list_3x3 = main.find_matrix_list_from_gen(GF, upper_triangular_general_matrix_1x1)

    cholesky_list = main.generate_cholesky_roots_matrices(GF, upper_triangular_list_3x3)

    # all cholesky roots of 1 x 1
    test_list = [np.array([[0]])]

    for cholesky_matrix in cholesky_list:
        found_match = False

        for i in range(0, len(test_list)):
            if((test_list[i] == cholesky_matrix).all()):
                test_list.pop(i)
                break
    # all cholesky roots should have been matched
    assert len(test_list) == 0

                

def two_by_two_matrix_test():
    """test the two by two upper trianglar matrix 
    test generation of all cholesky roots of 2x2
"""
    # general matrix
    upper_triangular_general_matrix_2x2 = np.array([[und, und],
                                                    [0,   und]], dtype="int16")

    # list that spans all possibilities from general matrix
    upper_triangular_list_2x2 = main.find_matrix_list_from_gen(GF, upper_triangular_general_matrix_2x2)

    for i, list in enumerate(upper_triangular_list_2x2):
        main.pretty_print_numpy_array(list, "list #" + str(i))

    cholesky_list = main.generate_cholesky_roots_matrices(GF, upper_triangular_list_2x2)


    test_list = [np.array([[0, 0], [0, 0]]),
                np.array([[0, 1], [0, 1]])]

    print("cholesky_list")
    print(cholesky_list)
    print("test list")
    print(test_list)

    assert len(cholesky_list) == len(test_list)

    for root in cholesky_list:
        assert test_list.count(root) == 1
        test_list.remove(root)


def three_by_three_matrix_test():
    """test the three by three upper triangular matrix 
    test generation of all cholesky roots of 3x3
    """
    # general matrix 
    upper_triangular_general_matrix_3x3 = np.array([[und, und, und],
                                                    [0,   und, und],
                                                    [0,   0,   und]], dtype="int16")

    # list that spans all possibilities from general matrix
    upper_triangular_list_3x3 = main.find_matrix_list_from_gen(GF, upper_triangular_general_matrix_3x3)

    cholesky_list = main.generate_cholesky_roots_matrices(GF, upper_triangular_list_3x3)


    test_list = [np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
                np.array([[0, 0, 0], [0, 0, 1], [0, 0, 1]]),
                np.array([[0, 0, 1], [0, 0, 0], [0, 0, 1]]),
                np.array([[0, 0, 1], [0, 0, 1], [0, 0, 0]]),
                np.array([[0, 1, 0], [0, 1, 0], [0, 0, 0]]),
                np.array([[0, 1, 1], [0, 1, 1], [0, 0, 0]])]
    
    for cholesky_matrix in cholesky_list:
        found_match_index = -1

        curr_index = 0
        while(curr_index < len(test_list) and found_match_index == -1):
            print("Compare ")
            print(test_list[curr_index])
            print("to")
            print(cholesky_matrix)
            print("at index " + str(curr_index))
            print((test_list[curr_index] == cholesky_matrix).all())
            if((test_list[curr_index] == cholesky_matrix).all()):
                print("match found at " + str(curr_index))
                found_match_index = curr_index
            print()
            curr_index += 1

        if(found_match_index != -1):
            test_list.pop(curr_index)
            print("--------------" + str(len(test_list)) + "--------------")
    # all cholesky roots should have been matched
    assert len(test_list) == 0




def run_all_tests():
    #one_by_one_matrix_test()
    two_by_two_matrix_test()
    #three_by_three_matrix_test()

run_all_tests()