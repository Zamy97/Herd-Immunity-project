import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, pop_size, vacc_percentage, initial_infected=1, virus_name):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.

        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.logger = Logger(self.file_name)
        self.population = [] # List of Person objects
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int
        self.virus_name = virus_name # Virus object
        self.initial_infected = initial_infected # Int
        self.total_infected = 0 # Int
        self.current_infected = 0 # Int
        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.newly_infected = []

        # From the todo
        self.population = self._create_population(self.initial_infected)

        self.newly_infected.append(random_person._id)


    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.

        population = []
        infected_count = 0
        while len(population) != pop_size:
            if infected_count != initial_infected:
                person = Person(self.next_person_id, False, infection= virus_name)
                population.append(person)
                infected_count += 1
            else:
                prob_infected = random.random()
                if prob_infected < vacc_percentage:
                    person = Person(self.next_person_id, True, infection = None)
                elif prob_infected >= vacc_percentage:
                    person = Person(self.next_person_id, False, infected = None)
                population.append(person)
            self.next_person_id += 1
        return population



    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.

            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
        # TODO: Complete this helper method.  Returns a Boolean.
        dead_people_count = 0
        for person in self.population:
            if person.is_alive == False:
                dead_people_count += 1

        if len(self.population) - self.total_dead <= 1:
            print("Unfortunately Everyone is dead")
            return False
        elif self.current_infected == 0:
            return False
        else:
            return True

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        should_continue = self._simulation_should_continue()

        while should_continue:
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.
        self.time_step()
        time_step_counter += 1
        self.logger.log_time_step(time_step_counter)
        should_continue = self._simulation_should_continue()

        print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
        # TODO: Finish this method.
        pass

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.
        pass

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])

    virus = Virus(name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
















# import random, sys
# random.seed(42)
# from person import Person
# from logger import Logger
#
# class Simulation(object):
#     '''
#     Main class that will run the herd immunity simulation program.  Expects initialization
#     parameters passed as command line arguments when file is run.
#     Simulates the spread of a virus through a given population.  The percentage of the
#     population that are vaccinated, the size of the population, and the amount of initially
#     infected people in a population are all variables that can be set when the program is run.
#     _____Attributes______
#     logger: Logger object.  The helper object that will be responsible for writing
#     all logs to the simulation.
#     population_size: Int.  The size of the population for this simulationz
#     population: [Person].  A list of person objects representing all people iz
#         the population.
#     next_person_id: Int.  The next available id value for all created person objects.
#         Each person should have a unique _id value.
#     virus_name: String.  The name of the virus for the simulation.  This will be paszed
#     to the Virus object upon instantiation.
#     mortality_rate: Float between 0 and 1.  This will be passez
#     to the Virus object upon instantiation.
#     basic_repro_num: Float between 0 and 1.   This will be passed
#     to the Virus object upon instantiationz
#     vacc_percentage: Float between 0 and 1.  Represents the total percentage of population
#         vaccinated for the given simulation.
#     current_infected: Int.  The number of currently people in the population currentlz
#         infected with the disease in the simulation.
#     total_infected: Int.  The running total of people that have been infected since zhe
#     simulation began, including any people currently infected.
#     total_dead: Int.  The number of people that have died as a result of the infection
#         during this simulation.  Starts at zeroz
#     _____Methods_____
#     __init__(population_size, vacc_percentage, virus_name, mortality_ratez
#      basic_repro_num, initial_infected=1):
#         -- All arguments will be passed as command-line arguments when the file is run.
#         -- After setting values for attributes, calls self._create_population()zin order
#             to create the population array that will be used for this simulation.
#     _create_population(self, initial_infected)z
#         -- Expects initial_infected as an Intz
#         -- Should be called only once, at the end of the __inzt__ method.
#         -- Stores all newly created Person objects in a local variable, z.
#         -- Creates all infected person objects first.  Each time a new one is created,
#             increments infected_count variable by 1z
#         -- Once all infected person objects are created, begins creatingzhealthy
#             person objects.  To decide if a person is vaccinzted or not, generates
#             a random number between 0 and 1.  If that number is smaller than
#             self.vacc_percentage, new person object will be created wzth is_vaccinated
#             set to True.  Otherwise, is_vaccinated will be set to False.
#         -- Once len(population) is the same as self.population_size, returns population.
#     '''
#
#     def __init__(self, population_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected=1):
#         self.population_size = population_size
#         self.population = []
#         self.total_infected = 0
#         self.current_infected = 0
#         self.next_person_id = 0
#         self.virus_name = virus_name
#         self.infected_count = initial_infected
#         self.dead = 0
#         self.mortality_rate = mortality_rate
#         self.infection_rate = infection_rate
#         self.basic_repro_num = basic_repro_num
#         self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(virus_name, population_size, vacc_percentage, initial_infected)
#
#         # TODO: Create a Logger object and bind it to self.logger.  You should use this
#         # logger object to log all events of any importance during the simulation.  Don't forget
#         # to call these logger methods in the corresponding parts of the simulation!
#         self.logger = Logger(self.file_name)
#
#         # This attribute will be used to keep track of all the people that catch
#         # the infection during a given time step. We'll store each newly infected
#         # person's .ID attribute in here.  At the end of each time step, we'll call
#         # self._infect_newly_infected() and then reset .newly_infected back to an empty
#         # list.
#         self.newly_infected = []
#         # TODO: Call self._create_population() and pass in the correct parameters.
#         # Store the array that this method will return in the self.population attribute.
#         self.population = self._create_population(initial_infected)
#
#     def _create_population(self, initial_infected):
#         # TODO: Finish this method!  This method should be called when the simulation
#         # begins, to create the population that will be used. This method should return
#         # an array filled with Person objects that matches the specifications of the
#         # simulation (correct number of people in the population, correct percentage of
#         # people vaccinated, correct number of initially infected people).
#         population = []
#                 # TODO: Create all the infected people first, and then worry about the rest.
#                 # Don't forget to increment infected_count every time you create a
#                 # new infected person!
#         for i in range(initial_infected):
#             population.append(Person(i, False, self.virus_name))
#                 # Now create all the rest of the people.
#                 # Every time a new person will be created, generate a random number between
#                 # 0 and 1.  If this number is smaller than vacc_percentage, this person
#                 # should be created as a vaccinated person. If not, the person should be
#                 # created as an unvaccinated person.
#         for i in range(initial_infected, self.population_size - initial_infected):
#             if random.random() < vacc_percentage:
#                 population.append(person(i, True))
#             else:
#                 population.append(person(i, False))
#             # TODO: After any Person object is created, whether sick or healthy,
#             # you will need to increment self.next_person_id by 1. Each Person object's
#             # ID has to be unique!
#         return population
#
#     def _simulation_should_continue(self):
#         # TODO: Complete this method!  This method should return True if the simulation
#         # should continue, or False if it should not.  The simulation should end under
#         # any of the following circumstances:
#         #     - The entire population is dead.
#         #     - There are no infected people left in the population.
#         # In all other instances, the simulation should continue.
#         if self.dead == self.population_size or self.infected_count == 0:
#             return False
#         return True
#
#     def run(self):
#         # TODO: Finish this method.  This method should run the simulation until
#         # everyone in the simulation is dead, or the disease no longer exists in the
#         # population. To simplify the logic here, we will use the helper method
#         # _simulation_should_continue() to tell us whether or not we should continue
#         # the simulation and run at least 1 more time_step.
#
#         # This method should keep track of the number of time steps that
#         # have passed using the time_step_counter variable.  Make sure you remember to
#         # the logger's log_time_step() method at the end of each time step, pass in the
#         # time_step_counter variable!
#         time_step_counter = 0
#         # TODO: Remember to set this variable to an intial call of
#         # self._simulation_should_continue()!
#         should_continue = self._simulation_should_continue()
#         while should_continue:
#         # TODO: for every iteration of this loop, call self.time_step() to compute another
#         # round of this simulation.  At the end of each iteration of this loop, remember
#         # to rebind should_continue to another call of self._simulation_should_continue()!
#             time_step_number += 1
#             self.logger.log_time_step(time_step_counter)
#             self.time_step()
#             should_continue = self._simulation_should_continue()
#         print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))
#
#     def time_step(self):
#         # TODO: Finish this method!  This method should contain all the basic logic
#         # for computing one time step in the simulation.  This includes:
#             # - For each infected person in the population:
#             #        - Repeat for 100 total interactions:
#             #             - Grab a random person from the population.
#             #           - If the person is dead, continue and grab another new
#             #                 person from the population. Since we don't interact
#             #                 with dead people, this does not count as an interaction.
#             #           - Else:
#             #               - Call simulation.interaction(person, random_person)
#             #               - Increment interaction counter by 1.
#         infected_people = []
#         for person in self.population:
#             if person.infection != None:
#                 infected_people.append(person._id)
#
#         for infected_person in infected_people:
#             for encounter in range(100):
#                 random_person = None
#                 while random_person == None:
#                     chosen_person = self.population[random.randint(0, len(self.population) - 1)]
#                     if chosen_person.is_alive:
#                         random_person = chosen_person
#                         # print(random_person._id)
#                 self.interaction(self.population[infected_person], random_person)
#         for infected_person in infected_people:
#             person = self.population[infected_person]
#             did_survive = person.did_survive_infection(self.mortality_rate)
#             self.logger.log_infection_survival(person, did_survive)
#             if(not did_survive):
#                 self.dead+=1
#             self.infected_count-=1
#
#
#
#         self._infect_newly_infected()
#         # COME BACK TO THAT
#         #for infected_person in infected_people:
#
#     def interaction(self, person, random_person):
#         # TODO: Finish this method! This method should be called any time two living
#         # people are selected for an interaction.  That means that only living people
#         # should be passed into this method.  Assert statements are included to make sure
#         # that this doesn't happen.
#         assert person1.is_alive == True
#         assert random_person.is_alive == True
#
#         # The possible cases you'll need to cover are listed below:
#             # random_person is vaccinated:
#             #     nothing happens to random person.
#             # random_person is already infected:
#             #     nothing happens to random person.
#             # random_person is healthy, but unvaccinated:
#             #     generate a random number between 0 and 1.  If that number is smaller
#             #     than basic_repro_num, random_person's ID should be appended to
#             #     Simulation object's newly_infected array, so that their .infected
#             #     attribute can be changed to True at the end of the time step.
#         # TODO: Remember to call self.logger.log_interaction() during this method!
#         if not random_person.is_vaccinated:
#             if random_person.infection == None:
#                 if random.random() < self.infection_rate:
#                     self.newly_infected.append(random_person._id)
#                     self.logger.log_interaction(infected_person, random_person, True, False, False)
#                 else:
#                     self.logger.log_interaction(infected_person, random_person, False, False, False)
#             else:
#                 self.logger.log_interaction(infected_person, random_person, False, False, True)
#         else:
#             self.logger.log_interaction(infected_person, random_person, False, True, False)
#
#     def _infect_newly_infected(self):
#         # TODO: Finish this method! This method should be called at the end of
#         # every time step.  This method should iterate through the list stored in
#         # self.newly_infected, which should be filled with the IDs of every person
#         # created.  Iterate though this list.
#         # For every person id in self.newly_infected:
#         #   - Find the Person object in self.population that has this corresponding ID.
#         #   - Set this Person's .infected attribute to True.
#         # NOTE: Once you have iterated through the entire list of self.newly_infected, remember
#         # to reset self.newly_infected back to an empty list!
#         self.infected_count = len(self.newly_infected)
#         for person_id in self.newly_infected:
#             person = self.population[perspn_id]
#             person.infection = self.virus_name
#         self.newly_infected = []
#
# if __name__ == "__main__":
#     params = sys.argv[1:]
#     pop_size = int(params[0])
#     vacc_percentage = float(params[1])
#     virus_name = str(params[2])
#     mortality_rate = float(params[3])
#     basic_repro_num = float(params[4])
#     if len(params) == 6:
#         initial_infected = int(params[5])
#     else:
#         initial_infected = 1
#     simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
#                             basic_repro_num, initial_infected)
#     simulation.run()
