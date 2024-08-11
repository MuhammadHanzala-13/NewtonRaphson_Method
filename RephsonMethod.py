# newton raphson method
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

class RephsonMethod:
    def __init__(self, equation, initial_guess, tolerance=1e-6, max_iter=100):
        
        
        
        # first we Initializes the RephsonMethod class with the function, initial guess, tolerance, and maximum iterations.

        # Parameters we used in constructor:
        # equation (str): The function for which we want to find the root ,taken as a string.
        # initial_guess (float): Initial guess for the root.
        # tol (float): Tolerance for the root. The algorithm stops when to stop prpgram (it help us in preciseing in guessing answer)
        # max_iter (int): Maximum number of iterations.
        
        self.equation = equation
        self.initial_guess = initial_guess
        self.tolerance = tolerance
        self.max_iter = max_iter
        self.x = sp.symbols('x')
        self.func = sp.sympify(equation)
        self.df = sp.diff(self.func, self.x)
        self.func_lambdified = sp.lambdify(self.x, self.func, modules=['numpy','sympy'])
        self.df_lambdified = sp.lambdify(self.x, self.df, modules=['numpy','sympy'])
    
    def find_root(self):
        """
        Performs the Newton-Raphson method to find the root of the function.

        Returns:
        float: An approximation of the root.
        """
        x_n = self.initial_guess
        
        for i in range(self.max_iter):
            func_x_n = self.func_lambdified(x_n)
            df_x_n = self.df_lambdified(x_n)
            
            if abs(func_x_n) < self.tolerance:
                return x_n
            
            x_n = x_n - func_x_n / df_x_n
        
        raise ValueError("Root not found within the maximum number of iterations")
#                   using syntax   
'''  for trignomertic function [sin(3**2),cos()] for logarithrmic function [log(x); eq = log10(x)-1 => log(x,10); eq =ln(x)-2ln(x-1) => log(x) - 2*log(x - 1) ] 
            tan-1(x)-4π=0 => atan(x) - pi/4" cosec => csc(x)'''
def plot_function_and_root(equation, root, x_range=(-10, 10)):
        x_vals = np.linspace(x_range[0], x_range[1], 400)
        y_vals = sp.lambdify(sp.symbols('x'), sp.sympify(equation), modules=['numpy', 'sympy'])(x_vals)

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=f'Function: {equation}')
        plt.axhline(0, color='green', linewidth=0.5)
        plt.axvline(root, color='orange', linestyle='--', label=f'Root: {root:.6f}')
        plt.scatter(root, 0, color='red', zorder=5)
        plt.title('Function and Found Root')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)
        plt.show()


print("starting...")
print("Newton-Raphson method")
print("\n")
# Take user input for the equation and initial guess
equation = input("Enter the equation (in terms of x): ")
print("\n")
initial_guess = float(input("Enter the initial guess: "))

# now create an instance of RephsonMethod class
method_chk = RephsonMethod(equation, initial_guess)
try:
    root = method_chk.find_root()
    with open("RephsonMethod.txt",'a') as info:
        info.write(f"The root is for Equation : [{equation}] is : {round(root,6)}")
        print("\n")
        info.write("\n")

        # info.seek(0)#diplay the value in file from 0 index of (Fln)
        # print(info.readline())#diplay the value in file from 0 index of (Fln) in terminal :)
    
    # Reopen the file to read only the last line
    with open("RephsonMethod.txt", 'r') as info:
        lines = info.readlines()
        print(lines[-1])  # Print only the last line  

    # Plot the function and the root
    plot_function_and_root(equation, root)

except ValueError as e:
    print(e)


# ----------------------------checker code ----------
# import math

# def f(x):
#     return math.cos(x**3) - math.cos(x) + math.tan(2*x) + 2

# def df(x):
#     # Derivative of f(x) = cos(x**3) - cos(x) + tan(2*x) + 2
#     # Using chain rule and derivative formulas
#     return -3 * x**2 * math.sin(x**3) + math.sin(x) + 2 * (1 / (math.cos(2*x)**2))

# def newton_raphson(x0, tol=1e-5):
#     x = x0
#     for i in range(100):
#         fx = f(x)
#         dfx = df(x)
#         if abs(fx) < tol:
#             return x
#         if dfx == 0:  # Avoid division by zero
#             print("Derivative is zero. No solution found.")
#             return None
#         x = x - fx / dfx
#     print("Not converged within 100 iterations")
#     return x

# # Set initial guess
# x0 = 2  # You can adjust this value as needed

# # Find the root using Newton-Raphson method
# root = newton_raphson(x0)

# # Print the root)
# print("Root of the equation: ", root)
