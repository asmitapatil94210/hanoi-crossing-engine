# hanoi-crossing-engine
Python implementation of the Hanoi Crossing game engine with replay and random-play modes.

Project Structure
hanoi-crossing-engine/
├── src/
│   ├── models.py
│   ├── engine.py
│   ├── replay.py
│   ├── random_play.py
│   └── constants.py
├── tests/
|   ├── test_engine.py
└── README.md

Assumptions
1. Turn order is provided as input in both Replay and Random Play.
2. Skip is always a valid action and is chosen randomly with other valid moves.
3. Both players can move disks from the shared pole if the move follows Tower of Hanoi rules.
4. A player wins only when their own disks are fully moved to Pole 3, with Pole 1, Pole 2, and their hand empty.
5. Invalid moves do not change the game state, but the turn is still used.


Input Format
1. Replay Mode:

The input is provided through standard input (stdin).
N
<turn_order>
<move_1>
<move_2>
...
<move_k>

Where:
N – Number of disks per player.
turn_order – Space-separated sequence of players (A or B).
Each move is on a new line in one of the following formats:
Lift <pole>
Place <pole>
Skip

2. Random Play Mode:

The input contains:
N
<turn_order>

How to run:
cd hanoi-crossing-engine
python src/replay.py
python src/random_play.py

Design Decisions
1. Each pole is represented as a stack (Python list), with the last element as the top disk.
2. Player hands store either the held disk or None.
3. Player visibility is defined as a constant (1a-2-3a for Player A and 1b-2-3b for Player B).

AI Usage
AI tools were used to discuss design ideas, clarify ambiguous game rules, and review implementation decisions. The final implementation, assumptions, and code structure were written and integrated by me.