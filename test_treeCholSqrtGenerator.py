import numpy as np 
import pytest

import treeCholSqrtGenerator
import utils

UNDEFINED = -1

def test_2x2_chol_tree_over_GF2():
    GF = 2
    n = 2
    tree = treeCholSqrtGenerator.UT_Matrix_Tree(utils.is_chol_matrix, GF=GF, n=n)
    root = tree.root

    assert np.array_equal([[0, UNDEFINED], [0, UNDEFINED]], root.current_arr)
    assert count_non_None_children(root.children) == 2

    children_list = root.children

    # check first child
    assert np.array_equal([[0, 0], [0, 0]], children_list[0].current_arr)
    check_children_None(children_list[0])

    # check second child
    assert np.array_equal([[0, 1], [0, 1]], children_list[1].current_arr)
    check_children_None(children_list[1])

def test_2x2_sqrt_tree_over_GF2():
    GF = 2
    n = 2
    tree = treeCholSqrtGenerator.UT_Matrix_Tree(utils.is_sqrt_matrix, GF=GF, n=n)
    root = tree.root

    assert np.array_equal([[0, UNDEFINED], [0, 0]], root.current_arr)
    assert count_non_None_children(root.children) == 2

    children_list = root.children

    # check first child
    assert np.array_equal([[0, 0], [0, 0]], children_list[0].current_arr)
    check_children_None(children_list[0])

    # check second child
    assert np.array_equal([[0, 1], [0, 0]], children_list[1].current_arr)
    check_children_None(children_list[1])


def check_children_None(node):
    """Utility function to check if all children are None (leaf node check)"""
    for child in node.children:
        assert child is None

def count_non_None_children(child_list):
    """Count how many non None children are in the list"""
    return len(child_list) - child_list.count(None)

def compare_test_and_result_lists_utility(result_list, test_list):
    """Checks to see if result_list and test_list are equal"""
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