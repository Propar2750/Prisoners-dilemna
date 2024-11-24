import random
import mysql.connectoras sqltor
# The main function in which player 1 and player 2 complete
def main(player_1, player_2):
    player_1_moves = []
    player_2_moves = []
    score_1 = 0
    score_2 = 0
    for l in range(1, 201):
        player_1_move = player_1(player_2_moves)
        player_2_move = player_2(player_1_moves)
        player_1_moves.append(player_1_move)
        player_2_moves.append(player_2_move)
        if player_1_move == "defect" and player_2_move == "defect":
            score_1 += 1
            score_2 += 1
        elif player_1_move == "defect" and player_2_move == "cooperating":
            score_1 += 5
        elif player_2_move == "defect" and player_1_move == "cooperating":
            score_2 += 5
        elif player_1_move == "cooperating" and player_2_move == "cooperating":
            score_1 += 3
            score_2 += 3
        # print(f"{(player_1.__name__)} did {player_1_move} and {player_2.__name__} did {player_2_move}")
    print(f"{(player_1.__name__)} scored {score_1} and {player_2.__name__} scored {score_2}")
    final_scores[player_1.__name__] = final_scores[player_1.__name__] + score_1
    final_scores[player_2.__name__] = final_scores[player_2.__name__] + score_2


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
# --------- Participants End ---------

# Basic Setup Starts
list_of_players = [tit_for_tat, always_defect, friedman, joss, tester_1, generous_tit_for_tat, always_cooperate,
                   two_tits_for_tat, tit_for_two_tats, fun_random, ashwika_1, nasty_forgiving, nasty_not_forgiving]
population = {}
final_scores = {}
for i in range(0, len(list_of_players)):
    final_scores[list_of_players[i].__name__] = 0
# Basic Setup Ends

# A tournament of 200 rounds
def tournamnent():
    global final_scores

    for i in range(0, len(list_of_players)):
        for j in range(0, len(list_of_players)):

            main(list_of_players[i], list_of_players[j])
    final_scores = dict(sorted(final_scores.items(), key=lambda x: x[1], reverse=True))
    print(final_scores)
tournamnent()
a = 5 # Number of columns in the element of the dictionary
mycon =sqltor.connect(host=<host name>,user =<username>,passwd=<password>,database =<database>)
cursor=mycon.cursor()
for i in range(0,len(final_scores)):
  for j in range(0, a):
    cursor.execute()
    
df = pd.DataFrame(data=final_scores)
