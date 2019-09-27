import random


teams = ["R", "B"]


class Board:
    size = 8

    def __init__(self):
        self.b = []
        c = 0
        for i in range(self.size):
            inner_b = []
            for j in range(self.size):
                if i < 3 and c:
                    inner_b.append(str(c) + "B ")
                elif i > 4 and c:
                    inner_b.append(str(c) + "R ")
                else:
                    inner_b.append(str(c) + "  ")
                c = -c + 1
            c = -c + 1
            self.b.append(inner_b)

    def __str__(self):
        retval = ""
        for i in range(self.size + 1):
            retval += (chr(64+i) + "  ")
            if not i:
                for k in range(self.size):
                    retval += (str(k + 1) + "  ")
                retval += "\n"
            else:
                for j in range(self.size):
                    retval += str(self.b[i-1][j])
                retval += "\n"
        return retval




def main():
    states_prime = {"0": 0, "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "1": 0}
    actions = {"A": {"0": .5, "B": .5}, "B": {"A": .5, "C": .5}, "C": {"B": .5, "D": .5}, "D": {"C": .5, "E": .5}, "E": {"D": .5, "1": .5}}
    rewards = {"0": 0, "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "1": 1}
    alpha = .9
    gamma = .01
    for i in range(100):
        states = states_prime
        for j in range(1000):
            curr = "C"
            while not (curr == "0" or curr == "1"):
                old = curr
                curr = weighted_random_by_dct(actions[curr])
                states[old] += alpha*(rewards[curr]+gamma*(states[curr])-states[old])
        for state in actions:
            child_sum = 0
            for action in actions[state]:
                child_sum += states[action] + rewards[action]
            for action in actions[state]:
                actions[state][action] = (states[action]+rewards[action])/child_sum
    print(actions)


def weighted_random_by_dct(dct):
    rand_val = random.random()
    total = 0
    for k, v in dct.items():
        total += v
        if rand_val <= total:
            return k
    assert False, 'unreachable'


main()



