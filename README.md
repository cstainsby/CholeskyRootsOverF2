# Cholesky Roots And Sqrts Of Upper Triangular Matrices Over F2
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Undergrad Reasearch Spring 2022
## How To Run
Run through the main.py file
To run use: python main.py "runtype" "GF" "n" "--flags"
For more details about this command look at main.py's def main function header

### Software Required
To Install you need 
- Git ([instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
- python ([download here](https://www.python.org/downloads/))

Python Libraries
- Required for running base program
    - numpy
- Required for running tests(optional)
    - pytest


## About The Project
Of particular concern to this research project is the relationship between
the number of Cholesky roots (ChRts) and the number of upper-triangular
square roots (SqRts) of the zero matrix. It is known that ChRts=SqRts (see
https://arxiv.org/abs/2109.06130 for proof). However the proof is not constructive - it 
doesn’t show that there is a way to match them up - and therefore leads
to the questions:
- Is this just dumb luck or is there a reason for this bijection?
- Is there a way to pair each 2×2 Cholesky Roots to a 2×2 Square Root in
such a manner that it will inform how to pair off the 3 × 3 matrices, the
4 × 4 matrices, etc?
- Is there a rule that will transform n ×n Cholesky Roots into n ×n square
roots for all n ≥ 1?

Link to our group's Overleaf page [here](https://www.overleaf.com/project/61e7965045e1e5674344ba14)