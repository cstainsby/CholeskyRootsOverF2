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
        - --out_to [filename.txt] : output print to file

    Runtype
        runtype must be specified or error
        - chol : creates a chol tree
        - sqrt : creates a sqrt tree 
    
    example run: 
    python main.py chol 2 2 --list --out_to file.txt
    This would print a list of all cholesky leaf nodes over F=2 with size of n=2
    The printed contents will be output into a file which should be included in the args after --out_to

    python main.py sqrt 2 3 --tree --with_children
    This would print a tree with matrices of F=2 and size of n = 3 that include each nodes children

    """
    # -------------------------------
    # get info from sys
    # -------------------------------
    flags = [arg for arg in sys.argv[3:] if arg.startswith("--")]
    runtype = sys.argv[1]
    GF = int(sys.argv[2])
    n = int(sys.argv[3])

    print("You entered \nruntype: " + runtype + "\nGF: " + str(GF) + "\nn: " + str(n))
    print("With flags:")
    for flag in flags:
        print("    " + flag)

    # -------------------------------
    # check for invalid use of flags
    # -------------------------------

    # check that no flag is repeated
    for flag in flags:
        if flags.count(flag) > 1:
            print("Error, flag: " + flag + " appears more than once")
            return
    # check list and tree arent run together
    if flags.count("--list") and flags.count("--tree"):
        print("Error, cannot run both list and tree")
        return
    # check list isn't being run with --with_children
    if(flags.count("--list") and flags.count("--with_children")):
        print("Error, cannot run --list and --with_children")
        return
    # check out_to has a file following the flag
    if(flags.count("--out_to")):
        print("out check")
        index_in_args = flags.index("--out_to")
        index_of_file = index_in_args + 1
        if index_of_file >= len(flags):
            print("Error, file not included after --out_to")
            return
        filename = flags[index_of_file]
        if(filename.startswith(".") or not filename.endswith(".txt")):
            print("Error, invalid filename")
            return
        
    # -------------------------------
    # run the program
    # -------------------------------

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