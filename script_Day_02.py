import os
import pandas as pd

data=input("What is the filepath for the data? ")
puzzle_input = pd.read_csv(data,header=None)

def clean_input(DATAFRAME):
    DATAFRAME["opponent_shape"] = DATAFRAME[0].astype(str).str[0]
    DATAFRAME["your_shape"] = DATAFRAME[0].astype(str).str[2]
    cleaned_puzzle_input = DATAFRAME[["opponent_shape","your_shape"]].reset_index()
    cleaned_puzzle_input["opponent_shape"] = cleaned_puzzle_input["opponent_shape"].map({"A":"Rock","B":"Paper","C":"Scissors"})
    cleaned_puzzle_input["your_shape"] = cleaned_puzzle_input["your_shape"].map({"X":"Rock","Y":"Paper","Z":"Scissors"})
    return cleaned_puzzle_input

cleaned_input = clean_input(puzzle_input) 

win , draw, lose = [6,3,0]

rock_outcome_scores, paper_outcome_scores, scissors_outcome_scores = [[draw,lose,win],[win,draw,lose],[lose,win,draw]]

score_for_shape_selection = {"Rock":[1,rock_outcome_scores], "Paper":[2,paper_outcome_scores], "Scissors":[3,scissors_outcome_scores]}

round_totals=[]
for index, row in cleaned_input.iterrows():
    round_totals += [[score_for_shape_selection[row['your_shape']][0]]]
    if row['opponent_shape'] == "Rock" : round_totals[index] += [score_for_shape_selection[row["your_shape"]][1][0]]
    elif row['opponent_shape'] == "Paper" : round_totals[index] += [score_for_shape_selection[row["your_shape"]][1][1]]
    elif row['opponent_shape'] == "Scissors" : round_totals[index] += [score_for_shape_selection[row["your_shape"]][1][2]]
    
sum_of_rounds=[]
for item in round_totals: sum_of_rounds+=[sum(item)]
print("The final score is " + str(sum(sum_of_rounds)))

fixed_score_input = clean_input(puzzle_input) 
fixed_score_input["your_shape"] = fixed_score_input["your_shape"].map({"Rock":"Lose","Paper":"Draw","Scissors":"Win"})
fixed_score_input.rename(columns={"your_shape":"outcome"}, inplace=True)

rock, paper, scissors = [1,2,3]

win_shape_scores, draw_shape_scores, lose_shape_scores = [[paper,scissors,rock],[rock,paper,scissors],[scissors,rock,paper]]

score_for_outcome = {"Win":[6,win_shape_scores], "Draw":[3,draw_shape_scores], "Lose":[0,lose_shape_scores]}

round_totals=[]
for index, row in fixed_score_input.iterrows():
    round_totals += [[score_for_outcome[row['outcome']][0]]]
    if row['opponent_shape'] == "Rock" : round_totals[index] += [score_for_outcome[row["outcome"]][1][0]]
    elif row['opponent_shape'] == "Paper" : round_totals[index] += [score_for_outcome[row["outcome"]][1][1]]
    elif row['opponent_shape'] == "Scissors" : round_totals[index] += [score_for_outcome[row["outcome"]][1][2]]
    
sum_of_rounds=[]
for item in round_totals: sum_of_rounds+=[sum(item)]
print("The final score is " + str(sum(sum_of_rounds)))