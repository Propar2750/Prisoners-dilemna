import copy
import random

import pandas as pd

from participants import tit_for_tat, always_defect, friedman, joss, tester_1, generous_tit_for_tat, always_cooperate,\
    two_tits_for_tat, tit_for_two_tats, fun_random, ashwika_1, nasty_forgiving, nasty_not_forgiving, list_of_players

# Toggles:
noise = True  # If you want a random chance that the actions are misinterpreted
noise_intensity = 40  # 1 in (Noise_intensity) chance to do opposite
do_evolution_1 = False
do_evolution_2 = True
intensity = False
# Main input
population = {tit_for_tat: 10, always_defect: 10, joss: 10, ashwika_1: 10, nasty_forgiving: 10,
              friedman: 10,tester_1:10,generous_tit_for_tat:10,always_cooperate:10,two_tits_for_tat:10,
              tit_for_two_tats:10,fun_random:10,nasty_not_forgiving:10}  # The main population dictionary which stores the current populations
num_of_evolutions = 20  # Number of evolutions you want to do


# The main function in which player 1 and player 2 complete
def main(player_1, player_2):
    player_1_moves = []
    player_2_moves = []
    score_1 = 0
    score_2 = 0

    for round_number in range(1, 201):
        player_1_move = player_1(player_2_moves)
        player_2_move = player_2(player_1_moves)

        if noise:  # If noise == True
            x = random.randint(0, noise_intensity - 1)
            if x == 1:
                y = random.randint(0, 1)
                if y == 0:
                    if player_1_move == "defect":
                        player_1_move = "cooperating"
                    else:
                        player_1_move = "defect"
                elif y == 1:
                    if player_2_move == "defect":
                        player_2_move = "cooperating"
                    else:
                        player_2_move = "defect"
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
        player_1_moves.append(player_1_move)
        player_2_moves.append(player_2_move)

    final_scores[player_1.__name__] = final_scores[player_1.__name__] + score_1
    final_scores[player_2.__name__] = final_scores[player_2.__name__] + score_2


# Basic Setup Starts


population_list = []
total_people = 0

population_print = {x.__name__: population[x] for x in population}
list_of_participants = []
for i in population:
    for j in range(population[i]):
        total_people += 1
        list_of_participants.append(i)
# list_of_participants.append(tit_for_tat for i in range(0,30))
final_scores = {}
for i in range(0, len(list_of_players)):
    final_scores[list_of_players[i].__name__] = 0


# Basic Setup Ends

# A tournament of 200 rounds
def tournament():
    global final_scores

    for participant_1 in list_of_participants:
        for participant_2 in list_of_participants:
            main(participant_1, participant_2)
    final_scores = dict(sorted(final_scores.items(), key=lambda x: x[1], reverse=True))


def evolution_1():
    global final_scores, total_people
    population_list.append(copy.deepcopy(population_print))
    num_of_people_to_remove = (total_people * random.randint(3, 8)) // 100
    num_of_people_to_add = (total_people * random.randint(5, 10)) // 100
    total_people = total_people - num_of_people_to_remove + num_of_people_to_add
    population_per_capita = {x: final_scores[x.__name__] / population[x] for x in list(population.keys())}
    population_per_capita = dict(sorted(population_per_capita.items(), key=lambda x: x[1], reverse=True))
    while True:
        last_key = list(population_per_capita)[-1]
        if population[last_key] > num_of_people_to_remove:
            population[last_key] = population[last_key] - num_of_people_to_remove
            population_print[last_key.__name__] = population_print[last_key.__name__] - num_of_people_to_remove
            for i in range(0, num_of_people_to_remove):
                list_of_participants.remove(last_key)
            break
        else:
            for i in range(0, population[last_key]):
                list_of_participants.remove(last_key)
            num_of_people_to_remove = num_of_people_to_remove - population[last_key]
            population.pop(last_key)
            population_per_capita.pop(last_key)
            population_print.pop(last_key.__name__)

    first_key = list(population_per_capita)[0]
    population[first_key] = population[first_key] + num_of_people_to_add
    population_print[first_key.__name__] = population_print[first_key.__name__] + num_of_people_to_add
    for i in range(0, num_of_people_to_add):
        list_of_participants.append(first_key)

    final_scores = {}
    for i in range(0, len(list_of_players)):
        final_scores[list_of_players[i].__name__] = 0


# Making the growing population dependent on a higher ratio of score per capita as a percentage of all score per capita
def evolution_2():
    global final_scores, total_people

    # Appending the current population to the populations list which will be accessed later for the final output
    population_list.append(copy.deepcopy(population_print))

    # Defining a new dictionary {player_function: total income of player_function.__name__/population of player_function
    population_per_capita = {x: final_scores[x.__name__] / population[x] for x in list(population.keys()) if
                             population[x] != 0}

    # Defining a new variable total score which will be the additional of all per capita average incomes
    total_score = 0
    for i in population_per_capita.values():
        total_score += i

    # Defining a new variable since we cant change the total amount of people before the entire code has run so it
    # will be changed after
    total_population_change = 0

    # Defining a new variable which has the ratio of per capita income as a whole
    population_per_capita_ratio = {player: per_capita_income / total_score for player, per_capita_income in
                                   population_per_capita.items()}

    for player, value in population_per_capita_ratio.items():
        # 0 < Value < 1

        # final_p can turn out to be negative
        final_p = population[player] + round((value - (1 / len(population.keys())) + 0.005) * total_people)

        total_population_change = final_p - population[player]

        # If expected population is negative 1. Remove all the players. 2. Remove the key from population
        if final_p < 0:
            for a in range(0, population[player]):
                try:
                    list_of_participants.remove(player)
                except ValueError:
                    break
            else:
                print("I tried to remove nothing",player.__name__,population[player])
            population.pop(player)

        # If expected population is positive 1. Add or remove required amount of players
        elif final_p > population[player]:
            for a in range(0, final_p - population[player]):
                list_of_participants.append(player)
        elif final_p < population[player]:
            for a in range(0, population[player] - final_p):
                list_of_participants.remove(player)

        if final_p>0:
            population[player] = final_p
            population_print[player.__name__] = final_p
        else:
            population[player] = 0
            population_print[player.__name__] = 0
        # print(key.__name__,final_p,value,value*5*(1-value)*population[key])

    final_scores = {}
    for i in range(0, len(list_of_players)):
        final_scores[list_of_players[i].__name__] = 0
    total_people += total_population_change


if do_evolution_2:
    for i in range(1, num_of_evolutions+1):
        tournament()
        evolution_2()
        print("Evolution: ",i)
elif do_evolution_1:
    for i in range(1, num_of_evolutions+1):
        tournament()
        evolution_1()
        print("Evolution: ",i)
population_plot = {x.__name__: [] for x in list_of_players}
for dict in population_list:
    for key in population_plot:
        if key in dict:
            population_plot[key].append(dict[key])

        else:
            population_plot[key].append(0)

df = pd.DataFrame(data=population_plot)
print(df)
df.to_excel("population.xlsx", index=False)
print(population_plot)
