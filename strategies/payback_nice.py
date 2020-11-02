import argparse
from enum import Enum

class Choice(Enum):
    """Provides the two options for the prisoner's dilemma"""
    SILENT = "S"
    BETRAY = "B"

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return self.__repr__()

def parse_history(hist):
    """Turns a string of a history into a list of Choices"""
    return [Choice(c) for c in hist]


###############################
# YOUR STRATEGY HERE
###############################

STRATEGY_NAME = "Payback Nice"
AUTHOR = "Dummy"

def strategy(my_hist, opp_hist, round):
    """The logic of the strategy

    Inputs:
        my_hist: A list of Choices that I chose 
        opp_hist: A list of Choices that the opponent chose
        round: The round number

    Returns:
        A Choice for this round
    """
    # Only retaliates if the opponent betrayed the last 3 times in a row
    if round >= 3:
        if (opp_hist[-1] == Choice.BETRAY and
                opp_hist[-2] == Choice.BETRAY and
                opp_hist[-3] == Choice.BETRAY):
            return Choice.BETRAY

    return Choice.SILENT

###############################
# END YOUR STRATEGY
###############################


if __name__ == "__main__":
    # Get commandline arguments
    parser = argparse.ArgumentParser(f"The {STRATEGY_NAME} strategy")
    parser.add_argument('-m', type=str, default="", dest="my_hist",
                        help='My history of choices')
    parser.add_argument('-o', type=str, default="", dest="opp_hist",
                        help='The opponent\'s history of choices')
    parser.add_argument('--name', action='store_true',
                        help='Gets the name of the strategy')
    parser.add_argument('--author', action='store_true',
                        help='Gets the author of the strategy')
    args = parser.parse_args()

    if args.name:
        print(STRATEGY_NAME)
    elif args.author:
        print(AUTHOR)
    
    else:
        # Parse the histories and make sure they're valid
        me = parse_history(args.my_hist)
        opp = parse_history(args.opp_hist)
        assert len(me) == len(opp)

        # Run the strategy
        choice = strategy(me, opp, len(me))
        assert isinstance(choice, Choice)

        # Output the result
        print(choice)
