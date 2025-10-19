import numpy as np
import sympy as sym

def main(x0, y, tolerance, max_iterations):
    '''
    Args:
    x0: initial root's guess

    y: the equation expression converted into sympy format
    
    tolerance: the minimum difference between two consecutively calculated root approximations required to stop   the algorithm
    
    max_iterations: maximum number of algorithm's iteration allowed
    '''
    # Extract the symbol from the expression
    # y.free_symbols returns a set of all symbolic variables in the expression
    # list() converts the set to a list, [0] gets the first (and typically only) symbol
    # For example: if y = 3*x - exp(x), then y.free_symbols = {x}, so x gets assigned the symbol 'x'
    x = list(y.free_symbols)[0]
    
    print(f"f(x) is {y}")
    y_prime = sym.diff(y, x)
    print(f"f'(x) is {y_prime}")
    tolerance_decimal = 10**(-tolerance)
    for i in range(max_iterations):
        print("*****************")
        print(f"Iteration {i+1}")
        print(f"x_{i}= {x0}")
        y_eval = y.evalf(subs={x:x0})
        y_prime_eval = y_prime.evalf(subs={x:x0})
        x1 = x0 - (y_eval/y_prime_eval)
        diff = abs(x1-x0)
        print(f"f(x_{i}) = {y_eval}")
        print(f"f'(x_{i}) = {y_prime_eval}")
        print(f"x_{i+1} = {x1}")
        print(f"diff x_{i+1} - x_{i} = {diff}")
        if (diff < tolerance_decimal):
            x1 = round(x1, tolerance+3)
            print("*****************")
            print(f"After {i+1} iterations, the method has converged to: {x1}")
            return (x1)
        x0 = x1
    print(f"After {i+1} iterations, the method did not converge")
    return None

if __name__ == "__main__":
    # run example
    print("run example")
    print("           ")
    x, y = sym.symbols('x y')
    y = 3*x - sym.exp(x)
    main(x0= 0.5, y = y, tolerance =6, max_iterations= 100)
