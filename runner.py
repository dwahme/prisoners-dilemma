import argparse

class Simulation:
    """Holds the data and runs a simulation"""

    def __init__(self, strategy_1, strategy_2, rounds):
        self.strategy_1 = strategy_1
        self.strategy_2 = strategy_2
        self.rounds = rounds

        self.hist_1 = []
        self.hist_2 = []

    def __run():
        # TODO- probably will need subprocess
        pass

    def duel():
        # Runs the entire simulation
        pass

    def dump_results():
        # Calculates total time spent in jail
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Runs the prisoner\'s dilemma contest')
    parser.add_argument('iterations', metavar='n', type=int,
                        help='How many times to run each simulation')
    parser.add_argument('-a', type=str, dest="strat_1",
                        help='The first strategy')
    parser.add_argument('-b', type=str, dest="strat_2",
                        help='The second strategy')
    args = parser.parse_args()

    sim = Simulation(args.strat_1, args.strat_2, args.iterations)
