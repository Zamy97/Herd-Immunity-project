
import random

class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.virus_name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    # https://github.com/timomak/CS-1.1-Programming-Fundamentals
    # https://github.com/dmcg89/herdimmunity/blob/master/simulation.py
    # https://github.com/jshams/Herd-Immunity/blob/master/simulation.py
    # https://github.com/Product-College-Courses/CS-1.1-Programming-Fundamentals/blob/master/Herd_Immunity_Project/person.py
    # https://github.com/RinniSwift/Herd_Immunity_Project/blob/master/simulation.py
    # https://github.com/natepill/Herd-Immunity/blob/master/simulation.py#L233
    # https://github.com/ruhsane/Herd_Immunity_Project/blob/master/logger.py
    # https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches
    # https://docs.pytest.org/en/latest/example/index.html
    # https://docs.pytest.org/en/latest/usage.html
