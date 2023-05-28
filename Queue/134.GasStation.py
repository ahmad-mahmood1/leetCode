def canCompleteCircuit(gas, cost):
    start = 0
    balance = 0
    deficit = 0
    for i in range(len(gas)):
        balance = balance + gas[i] - cost[i]

        if balance < 0:
            deficit += balance
            start = i + 1
            balance = 0

    if balance + deficit >= 0:
        return start

    return -1


gas = [2, 3, 4]
cost = [3, 4, 3]

print(canCompleteCircuit(gas, cost))
