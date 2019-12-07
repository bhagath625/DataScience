## 1. R Functions as Alternatives to Loops ##

library(readr)
scores <- read_csv("scores.csv")

## 3. A Vectorized Function for If-Else Statements ##

tied_matches <- if_else(scores$home_goals == scores$away_goals, "tie", "did not tie")

## 4. Multiple Cases: Nesting Functions to Chain If-Else Statements ##

home_team_result <- if_else(scores$home_goals > scores$away_goals, "win",
                      if_else(scores$home_goals < scores$away_goals, "lose",
                        if_else(scores$home_goals == scores$away_goals, "tie", "")))

scores_2 <- scores %>% 
              mutate(home_team_result = home_team_result)

## 6. Grouping and Summarizing Data Frames ##

home_goals_sum <- scores %>%
    group_by(home_country) %>%
    summarize(sum(home_goals))

## 7. Summarizing a Data Frame by Multiple Variables ##

away_results <- scores %>% 
    group_by(away_country) %>%
    summarize(total = sum(away_goals), 
              average = mean(away_goals), 
              min = min(away_goals), 
              max = max(away_goals))

## 8. Chaining Functions Together Using the Pipe Operator ##

brazil_goals <- scores %>%
  filter(home_country == "Brazil" | away_country == "Brazil") %>%
  mutate(total_goals = home_goals + away_goals) %>%
  arrange(desc(total_goals))