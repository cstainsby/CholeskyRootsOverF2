import numpy as np 
import pytest

import treeCholSqrtGenerator

UNDEFINED = -1

def test_2x2_chol_tree_over_GF2():
    GF = 2
    n = 2
    root = treeCholSqrtGenerator.generate_tree(GF, n)

    assert root.current_arr == [[0, UNDEFINED], [0, UNDEFINED]]
    assert len(root.children) == 2

    children_list = root.children

    # check first child
    assert children_list[0].current_arr == [[0, 0], [0, 0]]

    # check second child
    assert children_list[1].current_arr == [[0, 1], [0, 1]]
