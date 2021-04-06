N, K = map(int, input().split(" "))

values = []
weights = []

max_dict = {}

for _ in range(N):
    w, v = map(int, input().split(" "))
    values.append(v)
    weights.append(w)

def knapsack(values, weights, n, W):
    if W <= 0 or n == 0:
        return 0
    
    if (n-1, W) in max_dict:
        return max_dict[(n-1, W)]

    res = 0
    if W >= weights[n-1]:
        res =  max(knapsack(values, weights, n-1, W), 
        knapsack(values, weights, n-1, W-weights[n-1]) + values[n-1])
    else:
        res = knapsack(values, weights, n-1, W)

    max_dict[(n-1, W)] = res
    return res
    

print(knapsack(values, weights, N, K))