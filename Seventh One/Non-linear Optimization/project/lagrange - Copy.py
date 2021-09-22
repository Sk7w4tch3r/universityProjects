# -----------------------------------------------------------
# (C) 2021 SBU
# Released under GNU Public License (GPL)
# email hdamghanian77@gmail.com
# github sk7w4tch3r
# -----------------------------------------------------------

from sympy import *
from copy import deepcopy
init_printing(use_unicode=True)

'''
    This is the implementation of the lagrangian multipliers for any given
number of variables in the objective function and there is no limit on the
number of constraints.
    Constraints must be of the equality form and all the elements must be
on one side and the RHS must be equal to zero.
    define the symbol of variable used in the objective function like the
exmaple below and define the objective and it's constraints respectively.
pack the constraints of any number and pass them to the lagrangianOptimizer
to get the optimum points.
    USE CASE:

>>> x1, x2 = symbols('x1 x2')
>>> def function(x):  # the function to be maximized
>>>     x1, x2 = x
>>>     return -4*x1**2-2*x2**2+30*x1+7*x2
>>> def constraint_1(x):
>>>     x1, x2 = x
>>>     return 2*x1+x2-10
>>> cons = [constraint_1([x1, x2])]
>>> print(lagrangianOptimizer(function([x1,x2]), 'x1 x2', cons))
'''





def lagrangianOptimizer(fun, sbls, constraints):

    print(f'the input function:\n {fun}\n')
    print(f'with respect to these/this constraints:\n {constraints}\n')
    x = [var for var in symbols(sbls)]
    l = [i for i in range(len(constraints))]
    l_symbol = 'l'
    l_symbols = ''
    for i in l:
        l_symbols += l_symbol+str(i)+' '

    # l: lagrange multipliers, (tuple or Symbol (single)) type
    if type(symbols(l_symbols)) == tuple:
        l = [var for var in tuple(symbols(l_symbols))]
        variables = x+l
        print(f'multiple constraints, with total variables:\n {variables}\n')
    else:
        assert type(symbols(l_symbols)) == Symbol
        l = symbols(l_symbols)
        l = [l]
        variables = deepcopy(x)
        variables.append(l[0])
        print(f'single constraint, total variables:\n {variables}\n')

    # builds the lagrangian equation
    constraints.append(0)
    sum_index = len(constraints)-1
    for i in range(len(constraints)-1):
        constraints[sum_index] += constraints[i]*l[i]
    lagrangian = fun-constraints[sum_index]
    print(f'lagrangian:\n {lagrangian}\n')
    
    # calculates the gradient of the lagrangian respect to
    # variables in the equation
    gradients = []
    print(f'lagrangian derivative respect to')
    for var in variables:
        gradients.append(diff(lagrangian, var))
        print(f'{var}: \t', diff(lagrangian, var))
    
    # solves the system of equations
    results = linsolve(gradients, variables)
    
    # calculates the hessian matrix
    hessian_matrix = hessian(fun, x)


    # p matrix
    p_gradients = gradients[-len(l):]
    p = []
    for grad in p_gradients:
        tmp_grad = []
        for var in x:
            tmp_grad.append(-1*diff(grad, var))
        p.append(tmp_grad)

    print(f'\nthe p matrix is:\n {p}')
    print(f'\nand the hessian matrix is:\n {hessian_matrix}')

    print(f'\nthe optimum point is at: {variables}')
    return(results)


# and here is the driver with sample 2 variable objective and one constraint
if __name__ == "__main__":
    
    x1, x2 = symbols('x1 x2')
    # the function to be maximized
    def function(x):
        x1, x2 = x
        return -4*x1**2-2*x2**2+30*x1+7*x2
    
    
    def constraint_1(x):
        x1, x2 = x
        return 2*x1+x2-10

    cons = [constraint_1([x1, x2])]

    print(lagrangianOptimizer(function([x1,x2]), 'x1 x2', cons))
