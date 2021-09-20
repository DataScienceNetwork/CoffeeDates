
initials = ['CRR', 'UCH', 'LDB', 'MCN', 'SLN']

def round_robin(initials):
    # A simple implementation to pair up everyone with each other exactly once
    # limit: every week one person will have no one to drink coffee with :(
    n = len(initials)
    pairs = []
    if n%2 == 0:
        weeks = n-1
    if  n%2 == 1:
        weeks = n
        initials = initials + [None]
        n += 1

    for i in range(weeks):
        weekpairs = []
        for l in range(n//2):
            pair = (initials[l], initials[n-(1+l)])
            if None not in pair:
                weekpairs.append(pair)
        pairs.append(weekpairs)
        initials.insert(1, initials.pop())
    return(pairs)

def find_name(pairs, name):
    for i in range(len(pairs)):
        if name in pairs[i]:
            return i
    return None

def round_robin_fix(initials, pairs):
    modified_pairs = []

    for i in range(len(pairs)):
        for name in initials:
            pos_i = find_name(pairs[i], name)
            if i < len(pairs)-1 and pos_i is None:
                for j in range(i+1, len(pairs)):
                    pos_j = find_name(pairs[j], name)
                    if pos_j is not None:
                        pair = pairs[j].pop(pos_j)
                        pairs[i].append(pair)
                        break
    pairs = [pair for pair in pairs if len(pair) > 0]
    return pairs


def validate(initials, pairs):
    # assert how many meetings people have each week - might work better as a unit test.
    per_week = []
    for week in pairs:
        counts = {name: 0 for name in initials}
        for pair in week:
            for name in pair:
                counts[name] += 1
        per_week.append(counts)
    return per_week

pairs = round_robin(initials)
print(pairs)
fixed_pairs = round_robin_fix(initials, pairs)

print(validate(initials, fixed_pairs))
