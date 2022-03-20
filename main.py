import sys

import simpleCholSqrtGenerator
import treeCholSqrtGenerator
import utils

def main():
    """
    How To Run
        python main.py [runtype] [GF] [n] [--flags]

    COMMAND LINE ARGS: 

    Flags: Specify how you want your tree to be output
        by default full tree including children are included in output
        NOTE: you can use multiple flags 
        - --tree : run to get tree
            - --with_children : only outputs the tree 
        - --list : run to get list of leaf nodes

    Runtype
        runtype must be specified or error
        - chol : creates a chol tree
        - sqrt : creates a sqrt tree 
    
    example run: 
    python main.py chol 2 2 --list
    This would print a list of all cholesky leaf nodes over F=2 with size of n=2

    python main.py sqrt 2 3 --tree --with_children
    This would print a tree with matrices of F=2 and size of n = 3 that include each nodes children

    """
    flags = [arg for arg in sys.argv[3:] if arg.startswith("--")]
    runtype = sys.argv[1]
    GF = int(sys.argv[2])
    n = int(sys.argv[3])

    print("You entered \nruntype: " + runtype + "\nGF: " + str(GF) + "\nn: " + str(n))
    print("With flags:")
    for flag in flags:
        print("    " + flag)

    # check for invalid use of flags
    if flags.count("--list") and flags.count("--tree"):
        print("Error, cannot run both list and tree")
        return
    if(flags.count("--list") and flags.count("--with_children")):
        print("Error, cannot run --list and --with_children")
        return

    if flags.count("--list"):
        #TODO: make this a tree leaf function 
        if runtype == "chol":
            simpleCholSqrtGenerator.generate_list_of_type_matrices("chol", GF, n)
        elif runtype == "sqrt":
            simpleCholSqrtGenerator.generate_list_of_type_matrices("sqrt", GF, n)
    elif flags.count("--tree"):
        if runtype == "chol":
            tree = treeCholSqrtGenerator.UT_Matrix_Tree(utils.is_chol_matrix, GF, n)
            tree.DFS_generate_tree()
        elif runtype == "sqrt":
            tree = treeCholSqrtGenerator.UT_Matrix_Tree(utils.is_sqrt_matrix, GF, n)
            tree.DFS_generate_tree()

        if flags.count("--with_children"):
            print("printing with child")
            tree.pretty_print_tree(with_children=True)
        else:
            print("printing w/o child")
            tree.pretty_print_tree(with_children=False)

if __name__ == "__main__":
    print("Starting main")
    main()