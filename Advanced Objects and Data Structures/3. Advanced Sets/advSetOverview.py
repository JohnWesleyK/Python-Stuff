S = set()

S.add(100)
S.add(200)
S           # {100, 200}

S.clear()
S           # set()

S1 = {100,200,300}
S2 = S1.copy()
S2              # {100, 200, 300}

S1              # {100, 200, 300}
S1.add(500)
S1              # {100, 200, 300, 500}
S2              # {100, 200, 300}

S1.difference(S2)   # {500}

S1 = {100,200,300}
S2 = {100,400,500}
S1.difference_update(S2)
S1      # {200, 300}

S1      # {200, 300}
S1.discard(200)
S1      # {300}

S1 = {10,20,30}
S2 = {10,20,40}
S1.intersection(S2)     # {10, 20}
S1                      # {10, 20, 30}
S1.intersection_update(S2)
S1                      # {10, 20}

S1 = {10,20}
S2 = {10,20,40}
S3 = {50}

S1.isdisjoint(S2)       # False
S1.isdisjoint(S3)       # True

S1                      # {10, 20}
S2                      # {10, 20, 40}
S1.issubset(S2)         # True

S2.issuperset(S1)       # True
S1.issuperset(S2)       # False

S1      # {10, 20}
S2      # {10, 20, 40}
S1.symmetric_difference(S2)     # {40}

S1.union(S2)    # {10, 20, 40}

S1.update(S2)
S1              # {10, 20, 40}
