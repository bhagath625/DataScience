## 1. Introduction to Writing Your Own Functions ##

library(readr)
scores <- read_csv("scores.csv")

## 2. Anatomy of a Function ##

mult_by_100 <- function(x) {
  x * 100
}

away_by_100 <- mult_by_100(scores$away_goals)

## 3. When to Write a Function ##

percentage_of_total <- function(x) {
  x/sum(x) * 100
}
    
home_goals_percentage <- percentage_of_total(scores$home_goals)
away_goals_percentage <- percentage_of_total(scores$away_goals)

## 4. Writing Functions with Two Variables as Arguments ##

percentage <- function(x,y) {
  xy_total = x + y  
  (x/xy_total) * 100 
}

home_percent <- percentage(x = scores$home_goals, y = scores$away_goals)

## 5. Writing Functions for Conditional Execution ##

percentage_no_na <- function(x,y) {
  if(x + y > 0) {
    xy_total = x + y 
    (x/xy_total) * 100
  } else {
    0
  }
} 

percentage_no_na(x = scores$away_goals[15], y = scores$home_goals[15])

## 6. Functions with More Than Two Arguments ##

adjust_yz <- function(x,y,z) {
  if (x >= 5 & x <= 10) {
    y * 2 
  } else {
    z - 1
  }
}

match_one <- adjust_yz(x = scores$match_id[1], y = scores$home_goals[1], z = scores$away_goals[1])
match_five <- adjust_yz(x = scores$match_id[5], y = scores$home_goals[5], z = scores$away_goals[5])