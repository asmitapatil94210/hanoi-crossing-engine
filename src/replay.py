from models import Action, GameState, Move, Player
from engine import apply_move, check_win

# Read the input from user
n = int(input())
turn_order = [Player(p) for p in input().split()]

moves = []
for i in range(len(turn_order)):
    parts = input().split()

    action = Action(parts[0].capitalize())
    pole = parts[1] if len(parts) > 1 else None
    moves.append(Move(action, pole))

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
    move = moves[i]
    apply_move(game, player, move)

    if check_win(game, player):
        print(f"Player {player.value} wins!")
        break