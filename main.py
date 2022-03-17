import sys

import simpleCholSqrtGenerator
import treeCholSqrtGenerator

def main():
    """
    How To Run
        python main.py [runtype] [GF] [n] [--flags]

    COMMAND LINE ARGS: 

    Flags: Specify how you want your tree to be output
        by default full tree including children are included in output
        NOTE: you can use multiple flags in a run
        - --with_children : only outputs the tree 
        - --leaves : only prints the leaf nodes of the tree(valid matrices)

    Runtype
        runtype must be specified or error
        - chol : creates a chol tree
        - sqrt : creates a sqrt tree 
    
    example run: 
    python treeCholSqrtGenerator.py --no_children --leaves chol
    This would print all cholesky leaf nodes with no children
    """
    flags = [arg for arg in sys.argv[3:] if arg.startswith("--")]
    runtype = sys.argv[1]
    GF = sys.argv[2]
    n = sys.argv[3]

    tree = treeCholSqrtGenerator.UT_Matrix_Tree(GF, n)
    if flags.count("--leaves"):
        #TODO: make this a tree leaf function 
        if runtype == "chol":
            simpleCholSqrtGenerator.generate_list_of_type_matrices(GF, n, "chol")
        elif runtype == "sqrt":
            simpleCholSqrtGenerator.generate_list_of_type_matrices(GF, n, "sqrt")
    else:
        tree = treeCholSqrtGenerator.UT_Matrix_Tree(GF, n)
        tree.DFS_generate_tree()

        if flags.count("--with_children"):
            tree.pretty_print_tree(with_children=True)
        else:
            tree.pretty_print_tree(with_children=False)

    if len(sys.argv) < 2:
        print("incorrect ammount of arguments entered")
    else:
        # parse through the args
        for arg_index in range(len(sys.argv) - 1):
            remaining_args = len(sys.argv) - arg_index

            if remaining_args > 2:
                # then we have flags that have been entered
                pass
            else:
                # then we only have GF and n to read in
                pass
