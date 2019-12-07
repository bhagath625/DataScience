## 1. Introduction to Control Structures ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below
library(readr)
scores <- read_csv("scores.csv")

## 2. Introduction to the Data ##

scores_five <- scores[1:5,]
home_team_won <- c("home team won", "home team won", "home team did not win", "home team won", "home team won")
scores_five <- scores_five %>%
    mutate(home_team_won = home_team_won)

## 3. Selection: Writing Conditional Statements ##

if (scores$home_goals[3] > scores$away_goals[3]) {
  print("home team won")
} else {
  print("home team did not win")
}

## 4. Repetition: Writing For-Loops ##

for (country in scores$home_country) {
  print(country)
}

## 5. Looping Over Rows of a Data Frame ##

for (i in 1:nrow(scores)) { 
  print(scores$home_goals[i] - scores$away_goals[i]) 
}

## 6. Nested Control Structures ##

for (i in 1:nrow(scores)) {  
  if (scores$home_goals[i] > scores$away_goals[i]) {
    print(TRUE)
  } else {
    print(FALSE) 
  }
}

## 7. Storing For-Loop Output in Objects ##

home_team_won <- c()

for (i in 1:nrow(scores)) {  
  if (scores$home_goals[i] > scores$away_goals[i]) {
    home_team_won <- c(home_team_won, TRUE)
  } else {
    home_team_won <- c(home_team_won, FALSE)
  }
}

## 8. More Than Two Cases ##

if (scores$home_goals[3] > scores$away_goals[3]) {
    print("win")
} else if (scores$home_goals[3] < scores$away_goals[3]) {
    print("lose")
} else if (scores$home_goals[3] == scores$away_goals[3]) {
    print("tie")
}

## 9. More Than Two Cases: Writing a For-Loop ##

home_team_result <- c()

for (i in 1:nrow(scores)) {  
  if (scores$home_goals[i] > scores$away_goals[i]) {
    home_team_result <- c(home_team_result, "win")
  } else if (scores$home_goals[i] < scores$away_goals[i]) {
    home_team_result <- c(home_team_result, "lose")
  } else if (scores$home_goals[i] == scores$away_goals[i]) {
    home_team_result <- c(home_team_result, "tie")
  }
}

scores <- scores %>%
    mutate(home_team_result = home_team_result)