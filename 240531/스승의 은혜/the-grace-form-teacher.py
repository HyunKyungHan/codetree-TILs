import copy

def count_affordable(mat, budget):
    cost = 0
    st_count = 0
    for i in range(len(mat)):
        cost += sum(mat[i])
        if budget >= cost:
            st_count += 1
    return st_count

def discount(mat, budget):
    max_std = 0
    for i in range(len(mat)):
        d_mat = copy.deepcopy(mat)
        d_mat[i][0] = d_mat[i][0]//2
        if count_affordable(d_mat, budget) > max_std:
            max_std = count_affordable(d_mat, budget)
    return max_std

if __name__ == '__main__':
    s_num, budget  = map(int, input().split())
    costs = []
    for i in range(s_num):
        costs.append(list(map(int, input().split())))
    costs.sort(key=sum)
    print(discount(costs, budget))