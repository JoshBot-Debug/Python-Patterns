from human.Human import Human
from human.female.Gender import Gender as fGender
from human.male.Gender import Gender as mGender
from human.abilities.Run import Run

if __name__ == "__main__":

    # Uses the Strategy pattern
    male = Human(mGender())
    female = Human(fGender())

    # Uses the Observer pattern
    female.run(Run())