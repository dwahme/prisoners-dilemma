import argparse
import glob
import operator
import os
from subprocess import Popen, PIPE

class Simulation:
    """Holds the data and runs a simulation"""

    def __init__(self, strategy_1, strategy_2, rounds):
        self.strategy_1 = strategy_1
        self.strategy_2 = strategy_2
        self.rounds = rounds

        self.hist_1 = ""
        self.hist_2 = ""

        self.time_1 = 0
        self.time_2 = 0

    def __run(self):
        strat_1_args = ["python3", self.strategy_1, 
                        "-m", self.hist_1, "-o", self.hist_2]
        strat_2_args = ["python3", self.strategy_2, 
                        "-m", self.hist_2, "-o", self.hist_1]

        # Get the next set of decisions
        strat_1 = Popen(strat_1_args, stdout=PIPE, stdin=PIPE)
        strat_2 = Popen(strat_2_args, stdout=PIPE, stdin=PIPE)

        # Get results
        out_1, _ = strat_1.communicate()
        out_2, _ = strat_2.communicate()
        out_1 = out_1.decode("utf-8").strip()
        out_2 = out_2.decode("utf-8").strip()

        return out_1, out_2

    def duel(self):
        for i in range(self.rounds):
            res_1, res_2 = self.__run()
            self.hist_1 += res_1
            self.hist_2 += res_2

        self.calc_time()

        return self.hist_1, self.hist_2

    def calc_time(self):
        # Calculates total time spent in jail
        for i in range(self.rounds):
            if self.hist_1[i] == "S" and self.hist_2[i] == "S":
                self.time_1 += 1
                self.time_2 += 1

            elif self.hist_1[i] == "S" and self.hist_2[i] == "B":
                self.time_1 += 3
                self.time_2 += 0

            elif self.hist_1[i] == "B" and self.hist_2[i] == "S":
                self.time_1 += 0
                self.time_2 += 3

            elif self.hist_1[i] == "B" and self.hist_2[i] == "B":
                self.time_1 += 2
                self.time_2 += 2

            else:
                return -1, -1
        
        return self.time_1, self.time_2

def run_all(folder, rounds):
    os.chdir(folder)
    files = [f for f in glob.glob("*.py")]
    sims = []

    for i, f_1 in enumerate(files):
        for f_2 in files[i:]:
            sim = Simulation(f_1, f_2, rounds)
            sim.duel()

            sims.append(sim)

    return sims

def dump_results(sims):
    res = {}

    print("Individual Results\n---------------")

    for s in sims:
        s_1 = s.strategy_1.split(".")[0]
        s_2 = s.strategy_2.split(".")[0]

        print(f"{s_1} vs {s_2}: {s.time_1}-{s.time_2}")
        res[s_1] = s.time_1 + res.get(s_1, 0)
        res[s_2] = s.time_1 + res.get(s_2, 0)

    print("\nOverall Scores\n----------------")

    for k, v in sorted(res.items(), key=operator.itemgetter(1)):
        print(f"{k}: {v}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Runs the prisoner\'s dilemma contest')
    parser.add_argument('iterations', metavar='n', type=int,
                        help='How many times to run each simulation')
    parser.add_argument('-a', type=str, dest="strat_1", default="",
                        help='The first strategy')
    parser.add_argument('-b', type=str, dest="strat_2", default="",
                        help='The second strategy')
    parser.add_argument('-f', type=str, dest="folder", default="",
                        help='The fodler containing all strategies to test')
    args = parser.parse_args()

    sim = Simulation(args.strat_1, args.strat_2, args.iterations)

    if args.strat_1 != "" and args.strat_2 != "":
        print(sim.duel(), sim.calc_time())

    elif args.folder != "":
        sims = run_all(args.folder, args.iterations)
        dump_results(sims)
