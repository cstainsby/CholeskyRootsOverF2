import math

# binom func
#sum of(binom(n : floor(n/2)-3j) - binom(n : floor(n/2)-3j-1) * (2^(floor(n/2) * ceil(n/2))-3j^2-j)
def chol_sqrt_binom_size_growth(q, n):
    """
    DESC:
    Finds the ammount of pssible sqrt or chol matrices given size and feild

    PARAMS:
    n(int): the size of the matrix (n x n)
    q(int): the feild the matrix is over

    RETURN:
    sum(int): the total ammount of possible chol or sqrt matrices at matrix size n x n 
    """
    sum = 0

    if n % 2 == 0:
        # for even n's
        n_term = math.floor(n/2)

        # the starting and ending j are rounded to make runnin on for loop possible
        ending_j = math.ceil(n_term/3)
        starting_j = math.floor(-(n_term + 1)/3)
        
        for j in range(starting_j, ending_j):
            top = n
            bottom = math.floor(n/2)-3*j
            last_expr = q **(math.floor(n/2) * math.ceil(n/2) -(3*j**2)-j)

            sum += (math.comb(top, bottom) - math.comb(top, bottom - 1)) * last_expr
    else:
        # for odd n's
        n_term = math.floor(n/2 - 1/2)

        # the starting and ending j are rounded to make runnin on for loop possible
        ending_j = math.ceil(n_term/3)
        starting_j = math.floor(-(n_term + 2)/3)
        
        for j in range(starting_j, ending_j):
            top = 2*n_term + 1
            bottom = n_term-3*j
            last_expr = q **(n_term**2 + n_term -(3*j**2)-2*j)

            sum += (math.comb(top, bottom) - math.comb(top, bottom - 1)) * last_expr
    return int(sum)

if __name__ == "__main__":
    # manual run here
    GF = 2
    n = 2

    num_matrices = chol_sqrt_binom_size_growth(GF, n)
    print(num_matrices)