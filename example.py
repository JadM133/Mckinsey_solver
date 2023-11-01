from mckinsey_solver import Producer, Animal, Environment

if __name__ == "__main__":
    """ This is an example of how to use the code to solve the Mckinsey environment game.
    
    Note 1: For both producers and animals, you need to give the name as the first argument. As a 
    piece of advice, use the names AS THEY ARE, since some times the names might be similar and it
    might get confusing.
    
    Note 2: For producers, you only need the calories provided. For animals, you will calories needed, followed
    by calories provided, and any organisms that they can eat (defined by their NAMES given).
    
    Note 3: The code is completely fine with defining more Animals. You will have to add these to the list given
    as an argument for the Environemnt class."""

    prodA = Producer("ProdA", 5500)  # For producers, only give the name given and calories produced
    prodB = Producer("ProdB", 5000)
    prodC = Producer("ProdC", 4000)
    animal1 = Animal("Animal1", 4000, 3500, ['ProdA', 'ProdB'])  # For animals, give
    animal2 = Animal("Animal2", 3300, 4000, ['Animal1'])
    animal3 = Animal("Animal3", 4500, 3900, ['ProdB', 'ProdC'])
    animal4 = Animal("Animal4", 3800, 3700, ['Animal3', 'Animal5'])
    animal5 = Animal("Animal5", 3200, 2000, ['ProdC'])
    animal6 = Animal("Animal6", 2500, 1000, ['ProdB'])
    env = Environment([animal1, animal2, animal3, animal4, animal5, animal6], [prodA, prodB, prodC])
    env.is_sustainable()