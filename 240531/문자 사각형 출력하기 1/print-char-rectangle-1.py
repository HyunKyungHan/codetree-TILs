def alphabets():
    alpha = 'ABCDEFGHIJKMNOPQRSTUVWXYZ'
    alpha_list = []
    for i in range(len(alpha)):
        alpha_list.append(alpha[i])  
    return alpha_list

def matrix(mat):
    chars = alphabets()
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if len(chars) == 0:
                chars = alphabets()
            mat[j][i] = chars.pop(0)
    return mat

if __name__ == '__main__':
    N = int(input())
    init = [[0]*N for _ in range(N)]
    sol = matrix(init)
    for i in range(N):
        for j in range(N):
            print(sol[i][j], end=' ')
        print()