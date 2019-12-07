## 3. Importing Data into R ##

library(readr)
recent_grads <- read_csv("recent_grads.csv")

## 5. Indexing Data Frames ##

college_majors <- recent_grads$Major
unemployment_subset <- recent_grads[c(1,3,5), "Unemployment_rate"]

## 6. Selecting Data Columns ##

recent_grads_select <- recent_grads %>%
    select(Major, Major_category, Total, Men, Women, Median, Unemployment_rate)

## 7. Adding a New Column ##

recent_grads_select <- recent_grads %>%
    select(Major, Major_category, Total, Men, Women, Median, Unemployment_rate)
recent_grads_select <- recent_grads_select %>%
  mutate(Women_percent = (Women / Total) * 100)

## 8. Filtering by a Single Condition ##

recent_grads_health <- recent_grads_select %>%
    filter(Major_category == "Health")

recent_grads_money <- recent_grads_select %>%
    filter(Median > 70000)

## 9. Filtering by Multiple Conditions: Meeting At Least One Criterion ##

recent_grads_science <- recent_grads_select %>%
  filter(Major_category == "Biology & Life Science" | Major_category == "Physical Sciences")

## 10. Filtering by Multiple Conditions ##

potential_majors <- recent_grads_science %>%
  filter(Women_percent > 40 & Median >= 40000)

## 11. Arranging Data Frames by Variables ##

my_majors <- potential_majors %>% 
  arrange(Unemployment_rate, desc(Median))