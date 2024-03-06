import random

# ------- Participants --------
def tit_for_tat(previous_moves):
    # Does whatever the opponent did in the previous move
    if len(previous_moves) == 0:
        return "cooperating"
    else:
        return previous_moves[-1]


def generous_tit_for_tat(previous_moves):
    # There is a 10% chance to be co-operating otherwise it does whatever the opponent did in the previous move
    x = random.randint(0, 7)
    if len(previous_moves) == 0:
        return "cooperating"
    elif x == 1:
        return "cooperating"
    else:
        return previous_moves[-1]


def always_defect(previous_moves):
    # Always defects
    return "defect"


def always_cooperate(previous_moves):
    # Always cooperates
    return "cooperating"


def friedman(previous_moves):
    # Holds Grudges
    if "defect" in previous_moves:
        return "defect"
    else:
        return "cooperating"


def joss(previous_moves):
    # Sneaky (10% Chance to randomly deflect) otherwise it does whatever the opponent did in the previous move
    x = random.randint(0, 9)
    if x == 0:
        return "defect"
    elif len(previous_moves) == 0:
        return "cooperating"
    else:
        return previous_moves[-1]


def tester_1(previous_moves):
    # Tests the other persons strategy for the first two moves
    if len(previous_moves) == 0:
        return "defect"
    elif len(previous_moves) == 1:
        return "cooperating"
    elif len(previous_moves) == 2:
        return "cooperating"
    elif len(previous_moves) >= 3:
        if previous_moves[1] == "defect" and previous_moves[2] == "cooperating":
            # Also a losing condition
            if len(previous_moves) % 2 == 1:
                return "defect"
            else:
                return "cooperating"
        elif previous_moves[1] == "defect" and previous_moves[2] == "defect":
            return "defect"  # Loosing condition
        elif previous_moves[1] == "cooperating":
            return "defect"


def two_tits_for_tat(previous_moves):
    # Defects Twice if opponent defected once
    if len(previous_moves) == 0:
        return "cooperating"
    elif previous_moves[-1] == "defect":
        return "defect"
    elif len(previous_moves) >= 2 and previous_moves[-2] == "defect":
        return "defect"
    else:
        return "cooperating"


def tit_for_two_tats(previous_moves):
    # Defects once if opponent defected twice
    if len(previous_moves) <= 1:
        return "cooperating"
    elif previous_moves[-1] == "defect" and previous_moves[-2] == "defect":
        return "defect"
    else:
        return "cooperating"


def fun_random(previous_moves):
    x = random.randint(0, 1)
    if x == 0:
        return "defect"
    else:
        return "cooperating"


def ashwika_1(previous_moves):
    # two tit for two tat, two cooperating means forgiveness
    store = "cooperating"
    if len(previous_moves) == 0:
        return "cooperating"
    elif "defect" in previous_moves:

        no = 0
        for i in range(len(previous_moves) - 1, -1, -1):

            if previous_moves[i - 1] == "defect" and previous_moves[i] == "defect":
                store = "defect"
                no = i
                break
        for i in range(len(previous_moves) - 1, no, -1):
            if previous_moves[i] == "cooperating" and previous_moves[i - 1] == "cooperating":
                store = "cooperating"
                break
    return store


def nasty_forgiving(previous_moves):
    # Nasty, forgiving, Retaliatory
    x = random.randint(0, 6)
    if x == 1:
        return "defect"
    elif x == 2:
        return "cooperating"
    elif len(previous_moves) == 0:
        return "cooperating"
    else:
        return previous_moves[-1]


def nasty_not_forgiving(previous_moves):
    # Nasty, forgiving, Retaliatory
    x = random.randint(0, 6)
    if x == 1:
        return "defect"

    elif "defect" in previous_moves:
        return "defect"

    elif x == 2:
        return "cooperating"

    else:
        return "cooperating"
