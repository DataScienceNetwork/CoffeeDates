
initials = ["AAA", "BBB", "CCC", "DDD"]
history = [
  [("AAA", "BBB"), ("AAA", "CCC")],
  [("BBB", "CCC"), ("AAA", "CCC")]
]

def calculate_weights(initials, history):
    pair_dict = {}
    for i in range(len(initials)):
        for j in range(i+1,len(initials)):
            for k in range(len(history)-1,-1,-1):
                if (initials[i], initials[j]) in history[k]:
                    pair_dict[(initials[i], initials[j])] = k+1
                    break
    return pair_dict


def fitness(initials, pair_dict, next_pairing):
    return None
    
scipy.optimize.minimize(fitness, x0, args=(), method=None, jac=None, hess=None, hessp=None, bounds=None, constraints=(), tol=None, callback=None, options=None)