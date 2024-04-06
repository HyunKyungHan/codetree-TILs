def winner(scores_dict, former_winner):
    global cnt
    winner = None
    if scores['A'] > scores['B']:
        winner = 'A'
    elif scores['A'] < scores['B']:
        winner = 'B'
    else:
        winner = 'both'
    if winner != former:
        cnt += 1
    return winner, cnt


if __name__ == '__main__':
    n = int(input())
    scores = {'A': 0, 'B': 0}
    cnt = 0
    former = 'both'

    for i in range(n):
        who, score = input().split()
        scores[who] += int(score)
        former, cnt = winner(scores, former)
        
    print(cnt)