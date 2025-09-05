# Import all functions from participants_2.py
from continuous_pd_players import tit_for_tat, always_defect, friedman, joss, tester_1, generous_tit_for_tat, always_cooperate,\
    two_tits_for_tat, tit_for_two_tats, fun_random, ashwika_1, nasty_forgiving, nasty_not_forgiving
import pandas as pd

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
        try:
            score_1 += 5 - (player_2_move/10)
            score_2 += 5 - (player_1_move/10)
        except Exception as e:
            print("I was here",e,"Player 1 move",player_1.__name__,"I moved",player_2_move)
            pass
        if player_1_move > player_2_move:
            score_1 += 0.5
            score_2 -= 0.5
        elif player_1_move < player_2_move:
            score_1 -= 0.5
            score_2 += 0.5
        else:
            score_1 +=1
            score_2 +=1
        # print(f"{(player_1.__name__)} did {player_1_move} and {player_2.__name__} did {player_2_move}")
    print(f"{(player_1.__name__)} scored {score_1} and {player_2.__name__} scored {score_2}")
    final_scores[player_1.__name__] = final_scores[player_1.__name__] + score_1
    final_scores[player_2.__name__] = final_scores[player_2.__name__] + score_2

# I have noticed that when the same player competes against themselves the score added to that player is essentially double , which i do not consider to be a problem right now ,
# if somebody does consider that to be a problem it can be easily fixed by changing the iterations accordingly 



# Basic Setup Starts
list_of_players = [tit_for_tat, always_defect, friedman, joss, tester_1, generous_tit_for_tat, always_cooperate,
                   two_tits_for_tat, tit_for_two_tats, fun_random, ashwika_1, nasty_forgiving, nasty_not_forgiving]
# list_of_players = [tit_for_tat, fun_random]
population = {}
final_scores = {}
for i in range(0, len(list_of_players)):
    final_scores[list_of_players[i].__name__] = 0
# Basic Setup Ends

# A tournament of 200 rounds
def tournament():
    global final_scores

    for i in range(0, len(list_of_players)):
        for j in range(0, len(list_of_players)):

            main(list_of_players[i], list_of_players[j])
    final_scores = dict(sorted(final_scores.items(), key=lambda x: x[1], reverse=True))
    print(final_scores)
tournament()
df = pd.DataFrame(list(final_scores.items()), columns=['Player', 'Score'])
df.to_excel("population.xlsx", index=False)
