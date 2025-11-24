
def mochila_pacientes(pacientes, tiempo_max):
    n = len(pacientes)

    # DP (n+1) x (tiempo_max+1)
    dp = [[0] * (tiempo_max + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        gravedad = pacientes[i-1]["gravedad"]
        tiempo   = pacientes[i-1]["tiempo"]

        for t in range(1, tiempo_max + 1):
            if tiempo <= t:
                dp[i][t] = max(dp[i-1][t], dp[i-1][t-tiempo] + gravedad)
            else:
                dp[i][t] = dp[i-1][t]

    # reconstrucción del subconjunto óptimo
    t = tiempo_max
    seleccionados = []

    for i in range(n, 0, -1):
        if dp[i][t] != dp[i-1][t]:
            seleccionados.append(pacientes[i-1])
            t -= pacientes[i-1]["tiempo"]

    seleccionados.reverse()
    return seleccionados, dp[n][tiempo_max]

