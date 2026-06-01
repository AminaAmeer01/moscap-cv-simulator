"""
Frequency-dependent MOS capacitance models.
"""


def high_frequency_capacitance(Cox, Cs):
    """
    High-frequency MOS capacitance.

    Minority carriers cannot respond to the AC signal.
    The measured capacitance is the series combination
    of oxide and depletion capacitances.

    Parameters
    ----------
    Cox : float
        Oxide capacitance
    Cs : float
        Semiconductor capacitance

    Returns
    -------
    float
        High-frequency capacitance
    """

    return 1 / (1 / Cox + 1 / Cs)


def low_frequency_capacitance(Cox):
    """
    Low-frequency MOS capacitance.

    Minority carriers follow the AC signal.

    Returns
    -------
    float
        Low-frequency capacitance
    """

    return Cox