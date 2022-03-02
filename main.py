import sys

def main():
    """
    COMMAND LINE ARGS:
        in command line, running this program will be in the form
        python main.py [generation_type] , GF, n
        *note* the flags in the square brackets are optional,
               the args in parentheses are required to run  
        
        generation_type flags:
            --tree  (tree)
            --list  (list output, generates all sqrt and chols in respective lists with no particular ordering)

    """

    if len(sys.argv) < 2:
        print("incorrect ammount of arguments entered")
    else:
        # parse through the args
        for arg_index in range(len(sys.argv) - 1):
            remaining_args = len(sys.argv) - arg_index

            if remaining_args > 2:
                # then we have flags that have been entered
            else:
                # then we only have GF and n to read in
