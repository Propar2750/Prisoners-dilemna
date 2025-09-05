import random

# ------- Participants --------
def tit_for_tat(previous_moves):
    # Does whatever the opponent did in the previous move
    if len(previous_moves) == 0:
        return 0
    else:
        return previous_moves[-1]


def generous_tit_for_tat(previous_moves):
    # There is a 10% chance to be co-operating otherwise it does whatever the opponent did in the previous move
    x = random.randint(0, 7)
    if len(previous_moves) == 0:
        return 0
    elif x == 1:
        return 0
    else:
        return previous_moves[-1]


def always_defect(previous_moves):
    # Always defects
    return 150


def always_cooperate(previous_moves):
    # Always cooperates
    return 0


def friedman(previous_moves):
    # Holds Grudges
    return max(previous_moves) if previous_moves else 0
    


def joss(previous_moves):
    # Sneaky (10% Chance to randomly deflect) otherwise it does whatever the opponent did in the previous move
    x = random.randint(0, 9)
    if x == 0:
        return 150
    elif len(previous_moves) == 0:
        return 0
    else:
        return previous_moves[-1]


def tester_1(previous_moves):
    # Tests the other persons strategy for the first two moves
    if len(previous_moves) == 0:
        return 150
    elif len(previous_moves) == 1:
        return 0
    elif len(previous_moves) == 2:
        return 0
    else:
        if previous_moves[1] == 150 and previous_moves[2] == 0:
            # Also a losing condition
            if len(previous_moves) % 2 == 1:
                return 150
            else:
                return 0
        elif previous_moves[1] == 150 and previous_moves[2] == 150:
            return 150  # Loosing condition
        elif previous_moves[1] == 0:
            return 150
        else:
            return previous_moves[-1]


def two_tits_for_tat(previous_moves):
    # Defects Twice if opponent defected once
    if len(previous_moves) == 0:
        return 0
    elif previous_moves[-1] == 150:
        return 150
    elif len(previous_moves) >= 2 and previous_moves[-2] == 150:
        return 150
    else:
        return 0


def tit_for_two_tats(previous_moves):
    # Defects once if opponent defected twice
    if len(previous_moves) <= 1:
        return 0
    elif previous_moves[-1] == 150 and previous_moves[-2] == 150:
        return 150
    else:
        return 0


def fun_random(previous_moves):
    x = random.randint(0, 150)
    return x


def ashwika_1(previous_moves):
    # two tit for two tat, two cooperating means forgiveness
    store = 0
    if len(previous_moves) == 0:
        return 0
    elif 150 in previous_moves:

        no = 0
        for i in range(len(previous_moves) - 1, -1, -1):

            if previous_moves[i - 1] == 150 and previous_moves[i] == 150:
                store = 150
                no = i
                break
        for i in range(len(previous_moves) - 1, no, -1):
            if previous_moves[i] == 0 and previous_moves[i - 1] == 0:
                store = 0
                break
    return store


def nasty_forgiving(previous_moves):
    # Nasty, forgiving, Retaliatory
    x = random.randint(0, 6)
    if x == 1:
        return 150
    elif x == 2:
        return 0
    elif len(previous_moves) == 0:
        return 0
    else:
        return previous_moves[-1]


def nasty_not_forgiving(previous_moves):
    # Nasty, forgiving, Retaliatory
    x = random.randint(0, 6)
    if x == 1:
        return 150

    elif 150 in previous_moves:
        return 150

    elif x == 2:
        return 0

    else:
        return 0
# --------- Participants End ---------
