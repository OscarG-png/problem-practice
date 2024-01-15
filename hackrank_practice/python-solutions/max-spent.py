def getMoneySpent(keyboards, drives, b):
    max_spent = -1

    for kb in keyboards:
        for drive in drives:
            total_cost = kb + drive
            if total_cost <= b and total_cost > max_spent:
                max_spent = total_cost
    return max_spent
