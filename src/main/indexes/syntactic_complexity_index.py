def calculate(sentences, words, clauses, dependent_clauses, t_units):
    mls = words / sentences
    sc = sentences / clauses
    sr = dependent_clauses / t_units
    return round(mls * sc * sr, 2)
