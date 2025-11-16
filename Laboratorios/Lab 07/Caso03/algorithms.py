def backpack(peso, valor, W):
    n = len(peso)
    
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(W + 1):
            if peso[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - peso[i - 1]] + valor[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    
    objetos = []
    j = W
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            objetos.append(i - 1)
            j -= peso[i - 1]
    
    objetos.reverse()
    return dp[n][W], objetos
