import itertools
import numpy as np
from operator import itemgetter


def find_next_to_be_eaten(eater):
    ls = np.array([elem.cal_prov for elem in eater.can_eat])
    return itemgetter(*np.argwhere(ls == np.max(ls)).reshape(-1).tolist())(eater.can_eat)


class Environment:
    """ Class defining an Environment that has both Animals and Producers."""
    def __init__(self, animals, producers):
        self.animals = animals  # 8 of them
        self.producers = producers  # 3 of them
        self.is_working = self.clean_can_eat()
        if self.is_working:
            self.can_eat_to_class()
        self.best_remaining_cals = 0
        self.best_animals = []
        self.best_producers = []

    def is_sustainable(self):
        for animal_vec in itertools.combinations(self.animals, 5):
            print(f"Trying the following combination : {animal_vec}")
            sub_env = Environment(list(animal_vec), self.producers)
            anim, prod, cal = sub_env.run_simulation()
            print("--------------------------------------------------")
            if cal > self.best_remaining_cals:
                self.best_animals = anim
                self.best_producers = prod
                self.best_remaining_cals = cal
        if self.best_remaining_cals != 0:
            print("Summary:")
            print(f"Best Animals chosen are {self.best_animals}")
            print(f"Best Producers chosen are {self.best_producers}")
            print(f"Best Remaining calories are {self.best_remaining_cals}")
        else:
            print("The env si not SUSTAINABLE.....")

    def find_next_to_eat(self):
        func = lambda x: 0 if x.cal_need == 0 else x.cal_prov
        ls_cal_prov = [func(elem) for elem in self.animals]
        return np.argmax(np.array(ls_cal_prov))

    def remaining_cals(self):
        return sum([elem.cal_prov for elem in self.animals]) + sum([elem.cal_prov for elem in self.producers])

    def run_simulation(self):
        is_working = self.is_working
        for _ in np.arange(len(self.animals)):
            if not is_working:
                break
            eater = self.animals[self.find_next_to_eat()]
            food = CombinedFood(find_next_to_be_eaten(eater))
            if food.cal_prov > eater.cal_need:
                food - eater.cal_need
                eater.cal_need = 0
                continue
            else:
                is_working = False

        if is_working:
            print("Worked!!!")
            print(f"Animals chosen are {self.animals}")
            print(f"Producers chosen are {self.producers}")
            print(f"Remaining calories are {self.remaining_cals()}")
            return self.animals, self.producers, self.remaining_cals()
        else:
            print("Couldn't find anything.")
            return self.animals, self.producers, 0

    def can_eat_to_class(self):
        for animal in self.animals:
            ls = []
            for elem in animal.can_eat:
                try:
                    ls.append(self.animals[list.index(self.animals, elem)])
                except ValueError:
                    ls.append(self.producers[list.index(self.producers, elem)])
            animal.can_eat = ls

    def clean_can_eat(self):
        for animal in self.animals:
            animal.can_eat = [elem for elem in animal.can_eat if (elem in self.animals) or (elem in self.producers)]
            if not animal.can_eat:
                return False
        return True


class Organism:
    """ Class for livin Organisms (wehter Animals or Producers)."""
    def __init__(self, name, calories_prov):
        self.cal_prov = calories_prov
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other


class Animal(Organism):
    """ A class for Animals."""
    def __init__(self, name, calories_need, calories_prov, can_eat):
        super().__init__(name, calories_prov)
        self.can_eat = can_eat
        self.cal_need = calories_need


class Producer(Organism):
    """ A class for Producers."""
    def __init__(self, name, calories_prov):
        super().__init__(name, calories_prov)


class CombinedFood:
    """ A class for when an Animal can eat multiple Organisms (same amount of calories provided)."""
    def __init__(self, org_vec):
        try:
            iter(org_vec)
            self.org_vec = org_vec
        except TypeError:
            self.org_vec = [org_vec]
        self.cal_prov = sum([elem.cal_prov for elem in self.org_vec])
        self.number = len(self.org_vec)

    def __sub__(self, other):
        for elem in self.org_vec:
            elem.cal_prov = elem.cal_prov - other/self.number
        return CombinedFood(self.org_vec)

    def __str__(self):
        return str([elem for elem in self.org_vec])

    def __repr__(self):
        return repr([elem for elem in self.org_vec])
