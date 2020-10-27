# prisoners-dilemma
For Holding the Prisoner's Dilemma Contest

## About

This runs a contest for the iterated prisoner's dilemma, an upgraded version of the prisoner's dilemma. Essentially, this is a battle royale to find the best strategy for handling what to do in the prisoner's dilemma. 

### The Prisoner's Dilemma

The rules for the basic prisoner's dilemma is as follows:
1. Two strategy are given a choice- whether to stay silent, or betray the other strategy
2. Depending on both of their choices, the strategy are assigned "prison time"
3. The goal is to come out with the minimum amount of prison time

Prison time is assigned as follows:
- If both strategy choose to stay silent, they both get 1 year
- If both strategy choose to betray, they both get 2 years
- If one strategy stays silent and the other betrays, the silent strategy gets 3 years and the betraying strategy gets 0 years

### The Iterated Prisoner's Dilemma

This is the same as the prisoner's dilemma, except it is run a large number of times between the two strategies (on the order or 200 or so times). Each strategy can see all the choices both strategies made before the current round, and can use that information to make their next decision.

For example, if Strategy A and Strategy B were preparing to make their decision for round 4, Strategy A would receive the following information:
- Strategy A's history: Silent, Silent, Betray
- Strategy B's history: Betray, Silent, Betray

Prison time is calculated as the sum of the total time for each individual round, using the calculation from the regular version of the prisoner's dilemma.

So, using the choices above, the time accumulated after round 3 for each strategy would be the following:
- Strategy A: 3 years + 1 year + 2 years = 6 years
- Strategy B: 0 years + 1 year + 2 years = 3 years

### The Prisoner's Dilemma Contest

Given a number of strategies, the contest will run each strategy against every other strategy, including itself.

The total time for each duel will then be accumulated for each strategy, and the strategies will be ranked based upon total prison time acquired. The best strategy will be the one with the lowest total prison time, and the worst strategy will be the one with the most total prison time.

## Creating a Strategy

The strategy design part is more important, and is intended for both programmers and non-programmers to be able to do.

### Strategy Design

First, please take a moment to write a few sentences about what you think the best strategy would look like. For the sake of this experiment, please do not look up on the internet what the best strategy is. You could describe the actual steps to implement the strategy ("betrays if all 3 of the previous opponent's choices were to stay silent", "betrays with a 30% chance", etc), or more general characteristics of the strategy ("tends to betray more often", "switches choices a lot", etc). Any description is fine; they do not have to conform to some standard.

The important part of this step is to determine what people think are characteristics of an optimal strategy, not to determine the actual optimal strategy. This is more important than finding an actual winner.

### Strategy Implementation

Please do the strategy design step first. Afterwards, if you want to submit a strategy, please use the provided template at `./template.py`. Copy `template.py` into the `./strategies` folder and implement the `strategy()` function.

While submitting your own implementation is preferred, it is ok to do some research on the internet if you so desire. You are also welcome to submit multiple strategies (maybe one before looking stuff up, and one afterwards).

If your perception of the characteristics of a winning strategy changed during the course of implementation, it would be preferred if you let me know.

## Usage

Each strategy will be written as a program. Specifically, in `./template.py`, all that needs to be done is to implement the `strategy()` function.

`./runner.py` can be used to run a duel between two strategies, or run a full prisoner's dilemma contest. Usage is as follows:
- `python3 runner.py -h`: information on how to run the program
- `python3 runner.py -a .<strategy_a> -b <strategy_b> <num_rounds>`: Runs Strategy A vs Strategy B in a duel for `<num_rounds>` rounds
- `python3 runner.py -f <folder> <num_rounds>`: Runs a full prisoner's dilemma contest for all strategies in folder `<folder>` for `<num_rounds>` rounds

### Example Usage

To run the Satan strategy (`./strategies/satan.py`) against the Jesus strategy (`./strategies/jesus.py`) for 10 rounds
```
python3 runner.py -a ./strategies/satan.py -b ./strategies/jesus.py 10
```

To run a contest between all strategies in the `./strategies` folder for 200 rounds each
```
python3 runner.py -f ./strategies/ 200
```
