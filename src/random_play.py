from engine import apply_move, check_win, get_valid_actions
import random
from models import  GameState, Player

# Read the input from user
n = int(input())
turn_order = [Player(p) for p in input().split()]

poles = dict()
poles['1a'] = []
poles['1b'] = []
poles['3a'] = []
poles['2'] = []
poles['3b'] = []

for i in range(n*2 - 1, 0, -2):        
    poles['1a'].append(i)
    poles['1b'].append(i + 1)

hands = dict()
hands[Player.A] = None
hands[Player.B] = None
game = GameState(n, poles, hands)

for i in range(len(turn_order)):
    player = turn_order[i]
    valid_actions = get_valid_actions(game, player)
    move = random.choice(valid_actions)
    apply_move(game, player, move)

    if check_win(game, player):
        print(f"Player {player.value} wins!")
        break

#print final state of hands and poles
print("Hands:")
for player, hand in hands.items():
    print(f"Player {player.value}: {hand}")

print("Poles:")
for pole, disks in poles.items():
    print(f"{pole}: {disks}")
print()