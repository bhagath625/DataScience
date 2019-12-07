## 1. Analyzing New York City Public Schools Data ##

combined <- read_csv("combined.csv")

combined <- combined %>%
  select(-SchoolName, -`SCHOOL NAME.y`, -Name, -`School Name`, -school_name, -`Location 1`) %>%
  rename(school_name = `SCHOOL NAME.x`)

## 2. Visualizing Relationships Between Variables Using Scatter Plots ##

ggplot(data = combined) +
  aes(x = frl_percent, y = avg_sat_score) +
  geom_point()

ggplot(data = combined) +
  aes(x = ell_percent, y = avg_sat_score) +
  geom_point()

ggplot(data = combined) +
  aes(x = sped_percent, y = avg_sat_score) +
  geom_point()

## 4. Gathering Data into Columns ##

combined_race <- combined %>%
  gather(key = "race", value = percent, asian_per:white_per)

ggplot(data = combined_race) +
  aes(x = percent, y = avg_sat_score, color = race) +
  geom_point()

## 6. Correlation Analysis: Measuring the Strength of Relationships Between Variables ##

cor(combined$avg_sat_score, combined$asian_per, use = "pairwise.complete.obs")

## 7. Creating and Interpreting Correlation Matrices ##

cor_mat <- combined %>%
  select_if(is.numeric) %>%
  cor(use = "pairwise.complete.obs")

## 8. Identifying Interesting Relationships ##

cor_tib <- cor_mat %>%
  as_tibble(rownames = "variable")
apscore_cors <- cor_tib %>%
  select(variable, high_score_percent) %>%
  filter(high_score_percent > 0.25 | high_score_percent < -0.25)