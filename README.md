# Mckinsey Solver:

The purpose of this tiny library is to solve the Mckinsey environment problem using python.

# Detailed installation guide:

- First clone the rep: git clone https://github.com/JadM133/Mckinsey_solver.git
- Second, after creating and activating your venv, install the library by: pip install .\Mckinsey_solver\
- Finally, run: python .\Mckinsey_solver\example.py to make sure the installation was successful.
- After that, you can create your own example by simply importing the classes as follows: from mckinsey_solver import Producer, Animal, Environment

# Notes for use:

- The example here is the one given in https://www.youtube.com/watch?v=4xpbD218sos. I just added a sixth animal to show that the code will take all available combinations of 5 animals. I advise that you try running the different scenarios discussed in the video within the code and make sure you get the same outcomes.
    
- YOU STILL HAVE WORK TO DO. You have to sort the animals and producers into three different categories (usually 3 of them, the ones that have the same temperatures and heigts, again check the youtube video!). These are usually 8 animals and 3 producers but could be more! (You could get up to 10 animals in the same category).
    
- Once you have the 8 animals (let's say) and 3 producers, give them as inputs in the main. You only need to provide the calories provided for producers, and the calories neded/provided and who can be eaten by animals as commented later in the main.
    
- Giving the animals and producers ad inputs takes time and you might need to try ALL 3 different sets!!! This process takes time so I advice you to type as fast as possible and don't underestimate the assignment because you have the code.

- BE CAREFUL: The name of the variables (animal1, animal2, etc.) is different than the name you are given (e.g. Shark). Please be sure to always use the names given as the first argument as the food of other animals.

- BE CAREFUL: If you decide to add more animals, you also have to add them in the environemnt by adding the variable name to the list (commented later in the code).
    
- Runtime: The code will print every combination tried (it will try all every possible combination of 5 animals with the three producers) and in the end, it will either print that the environment is not sustainable (no need to waste your time there then), or it will print a happy message with the combination having the largest remaining calories picked out for you.
    
- Good luck! If I can assist further, please contact me on jad.mounayer@outlook.com
