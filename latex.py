#!/usr/bin/env python

import sys
sys.dont_write_bytecode = True
sys.path.append("/usr/lib/latex-converter-package")
from ast_to_latex import latex_equation, RIGHT, LEFT

def display_diff(eq):
    return latex_equation(eq)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        eq = sys.argv[1]
        try:
            diff = display_diff(eq)
            print(f"\nThis is your equation in LaTeX: {display_diff(eq)}\n")
        except ValueError as e:
            print(e)
            sys.exit(0)
        except IndexError as e:
            print("Missing arguments")
            sys.exit(0)
        except Exception as e:
            print(e)
            print("Invalid Equation")
            sys.exit(0)
    else:
        print("Please enter your equation after calling the package, like so: latex-converter x^2")
