def high_frequency_capacitance(Cox, Cs):
    return 1 / (1 / Cox + 1 / Cs)


def low_frequency_capacitance(Cox):
    return Cox