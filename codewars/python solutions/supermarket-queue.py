def queue_time(customers, n):
    registers = [0] * n

    for customer in customers:
        min_register = min(registers)
        min_index = registers.index(min_register)
        registers[min_index] += customer

    return max(registers)
