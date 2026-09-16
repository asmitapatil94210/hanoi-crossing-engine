#test cases for engine functions: apply_move, check_win, and get_valid_actions
import pytest
from engine import apply_move, check_win, get_valid_actions
from models import Action, Move, Player, GameState

def test_apply_move_lift():
    poles = {
        '1a': [3, 1],
        '1b': [4, 2],
        '2': [],
        '3a': [],
        '3b': []
    }
    hands = {
        Player.A: None,
        Player.B: None
    }
    game = GameState(3, poles, hands)

    move = Move(Action.LIFT, '1a')
    apply_move(game, Player.A, move)
    assert game.hands[Player.A] == 1
    assert game.poles['1a'] == [3]

def test_apply_move_place():
    poles = {
        '1a': [3],
        '1b': [4, 2],
        '2': [],
        '3a': [],
        '3b': []
    }
    hands = {
        Player.A: 1,
        Player.B: None
    }
    game = GameState(3, poles, hands)

    move = Move(Action.PLACE, '3a')
    apply_move(game, Player.A, move)
    assert game.hands[Player.A] is None
    assert game.poles['3a'] == [1]

def test_check_win():
    poles = {
        '1a': [],
        '1b': [],
        '2': [],
        '3a': [3, 1],
        '3b': [4, 2]
    }
    hands = {
        Player.A: None,
        Player.B: None
    }
    game = GameState(3, poles, hands)
    assert check_win(game, Player.A) is True
    assert check_win(game, Player.B) is True

def test_get_valid_actions():
    poles = {
        '1a': [3, 1],
        '1b': [4, 2],
        '2': [],
        '3a': [],
        '3b': []
    }
    hands = {
        Player.A: None,
        Player.B: None
    }
    game = GameState(3, poles, hands)
    valid_actions = get_valid_actions(game, Player.A)
    assert Move(Action.LIFT, '1a') in valid_actions
    assert Move(Action.LIFT, '1b') in valid_actions
    assert Move(Action.SKIP, None) in valid_actions
    # Now test when the player is holding a disk
    game.hands[Player.A] = 1
    valid_actions = get_valid_actions(game, Player.A)
    assert Move(Action.PLACE, '3a') in valid_actions
    assert Move(Action.SKIP, None) in valid_actions
    # The player should not be able to place on a pole with a smaller disk
    assert Move(Action.PLACE, '1a') not in valid_actions
    assert Move(Action.PLACE, '1b') not in valid_actions
    assert Move(Action.PLACE, '2') in valid_actions
    assert Move(Action.PLACE, '3b') in valid_actions