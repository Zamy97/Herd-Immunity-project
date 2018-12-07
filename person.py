import random
random.seed(42)
from virus import Virus


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection  # Virus object or None

    def did_survive_infection(self):
        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        '''
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean
        prob_infected = random.random()
        if prob_infected < mortality_rate:
            self.is_alive = False
            return False
        else:
            self.is_vaccinated = True
            self.infection = None
            return True


''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...


def test_sick_person_instantiation():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(3, False, Ebola)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    assert person._id == 3
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is Ebola


def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, virus)

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
        assert person.is_alive is True
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who survived
        # assert ...
        assert person.is_vaccinated is True
    else:
        assert person.is_alive is False
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who did not survive
        # assert ...
        pass




# import random
# # TODO: Import the virus clase
#
# class Person(object):
#     '''
#     Person objects will populate the simulation.
#
#     _____Attributes______:
#
#     _id: Int.  A unique ID assigned to each person.
#
#     is_vaccinated: Bool.  Determines whether the person object is vaccinated against
#         the disease in the simulation.
#
#     is_alive: Bool. All person objects begin alive (value set to true).  Changed
#         to false if person object dies from an infection.
#
#     infection:  None or Virus object.  Set to None for people that are not infected.
#         If a person is infected, will instead be set to the virus object the person
#         is infected with.
#
#     _____Methods_____:
#
#     __init__(self, _id, is_vaccinated, infection=None):
#         - self.alive should be automatically set to true during instantiation.
#         - all other attributes for self should be set to their corresponding parameter
#             passed during instantiation.
#         - If person is chosen to be infected for first round of simulation, then
#             the object should create a Virus object and set it as the value for
#             self.infection.  Otherwise, self.infection should be set to None.
#
#     did_survive_infection(self):
#         - Only called if infection attribute is not None.
#         - Takes no inputs.
#         - Generates a random number between 0 and 1.
#         - Compares random number to mortality_rate attribute stored in person's infection
#             attribute.
#             - If random number is smaller, person has died from disease.
#                 is_alive is changed to false.
#             - If random number is larger, person has survived disease.  Person's
#             is_vaccinated attribute is changed to True, and set self.infection to None.
#     '''
#
#     def __init__(self, _id, is_vaccinated, infection_on_people=None):
#         # TODO:  Finish this method.  Follow the instructions in the class documentation
#         # to set the corret values for the following attributes.
#         self._id = _id
#         self.is_vaccinated = is_vaccinated
#         self.is_alive = True
#         self.infection_on_people = infection_on_people
#
#
#     def did_survive_infection(self):
#         # TODO:  Finish this method. Follow the instructions in the class documentation
#         # TODO: You will need to decide what parameters you pass into this method based on how you structure your class.
#         # for resolve_infection.  If person dies, set is_alive to False and return False.
#         # If person lives, set is_vaccinated = True, infection = None, return True.
#         get_random_number = random.random()
#         if get_random_number < mortality_rate:
#             self.is_alive = False
#             self.infection_on_people = None
#             return False
#         elif get_random_number > mortality_rate:
#             self.is_alive = True
#             self.vaccinated = True
#             self.infection_on_people = None
#             return True
