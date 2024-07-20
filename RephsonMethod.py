import sympy as sp

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
        self.func_lambdified = sp.lambdify(self.x, self.func, 'numpy')
        self.df_lambdified = sp.lambdify(self.x, self.df, 'numpy')
    
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

# Take user input for the equation and initial guess
equation = input("Enter the equation (in terms of x): ")
print("\n")
initial_guess = float(input("Enter the initial guess: "))

# now create an instance of RephsonMethod class
method_chk = RephsonMethod(equation, initial_guess)
try:
    root = method_chk.find_root()
    with open("RephsonMethod.txt",'a+') as info:
        info.write(f"The root is: {round(root,6)}")
        print("\n")
        info.write("\t \n")
        info.seek(0)#diplay the value in file from 0 index of (Fln)
        print(info.readline())#diplay the value in file from 0 index of (Fln) in terminal :)
    

except ValueError as e:
    print(e)
    

  
