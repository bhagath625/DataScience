## 1. Introducing Functionals ##

library(readr)
scores <- read_csv("scores.csv")

## 2. Working With Functionals From the Tidyverse purrr Package ##

match_results <- list(c(3,1), c(1,0), c(1,5), c(3,1), c(3,0))
names(match_results) <- c("match 1", "match 2", "match 3", "match 4", "match 5")
min_scores <- map(match_results, min)

## 3. Using Functionals to Apply Custom Functions ##

percentage_of_total <- function(x) {
  x/sum(x) * 100
}
per_goals_output <- scores %>%
  select(home_goals, away_goals) %>%
  map(percentage_of_total)

## 4. Functionals to Return Vectors of Specified Types ##

match_results <- list(c(3,1), c(1,0), c(1,5), c(3,1), c(3,0))
names(match_results) <- c("match 1", "match 2", "match 3", "match 4", "match 5")
sum_chr <- map_chr(match_results, sum)

typeof(sum_chr)

## 5. Functionals for Two-Variable Functions ##

percentage_no_na <- function(x,y) {
  if(x + y > 0) {
    xy_total = x + y 
    (x/xy_total) * 100
  } else {
     0
  }
}
percent_goals_home <- map2(scores$home_goals, scores$away_goals, percentage_no_na)

## 6. Functionals for Returning Vectors of Specific Types from Functions With Two Variables ##

percentage_no_na <- function(x,y) {
  if(x+y > 0) {
    total_goals = x+y 
    (x/total_goals) * 100
  } else {
    0
  }
}
scores_2 <- scores %>% 
  mutate(percent_goals_home = map2_dbl(scores$home_goals,scores$away_goals, percentage_no_na))

## 7. Functionals for Functions with More Than Two Variable Arguments ##

adjust_yz_2 <- function(x,y,z) {
  if (x >= 5 & x <= 10) {
    y * 2 
  } else {
    z - 1
  }
}
args_list <- list(x = scores$match_id, y = scores$home_goals, z = scores$away_goals)

adjusted_scores <- pmap_dbl(args_list, adjust_yz_2)