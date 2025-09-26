INITIAL_STATE = '.........'

def successor(state,player,index):
    return state[:index] + player + state[index+1:]

def legal_moves(state):
    return [i for i in range(9) if state[i] == '.']

def winner(state):
    rows = [[1,2,3],[3,4,5],[6,7,8],
            [0,3,4],[1,4,7],[2,5,8],
            [0,4,8], [2,4,6]]
    for a,b,c in rows:
        if (state[a] != '.') and (state[a] == state[b] == state[c]):
            return state[a]
    return '.'

def game_over(state):
    return (legal_moves(state) == []) or (winner(state) != '.') #?????

def value(state,player):
    if game_over(state):
        w = winner(state)
        return 'O.X'.find(w) - 1
    best_value = -2 if player =='X' else 2
    for m in legal_moves(state):
        v = value(successor(state,player,m),'O' if player=='X' else 'X')
        if (player == 'X' and v>best_value) or (player == 'O' and v <best_value): #here
            best_value = v
    return best_value

def best_move(state,player):
    best_value = -2 if player =='X' else 2
    best_play = None
    for m in legal_moves(state):
        v = value(successor(state,player,m),'O' if player=='X' else 'X')
        if (player == 'X' and v>best_value) or (player == 'O' and v <best_value): #here
            best_value, best_play = v,m
    return best_play

