def top_three_largest(values):
    # values: list of numbers
    # return the three largest values in descending order
    v = sorted(values, reverse=True)
    return v[:3] if len(v) > 2 else v