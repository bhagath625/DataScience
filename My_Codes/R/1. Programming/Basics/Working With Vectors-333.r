## 1. Indexing Vectors by Position ##

final_scores <- c(88, 87.66667, 86, 91.33333, 84, 91, 89.33333)
stem_grades <- final_scores[c(1,2)]
non_stem_grades <- final_scores[c(3:7)]

avg_stem_grades <- mean(stem_grades)
avg_non_stem_grades <- mean(non_stem_grades)

## 2. Numeric and Character Data Types ##

class_names <- c("math", "chemistry", "writing", "art", "history", "music", "physical_education")

## 3. Naming Elements of a Vector ##

class_names <- c("math", "chemistry", "writing", "art", "history", "music", "physical_education")
final_scores <- c(88, 87.66667, 86, 91.33333, 84, 91, 89.33333)
names(final_scores) <- class_names

## 4. Indexing Vectors Using Names ##

liberal_arts <- final_scores[c("writing", "history")]
fine_arts <- final_scores[c("art", "music")]

mean(liberal_arts)
mean(fine_arts)

## 5. Comparing Values And Logical Data Types ##

liberal_arts <- final_scores[c("writing", "history")]
fine_arts <- final_scores[c("art", "music")]
mean(liberal_arts) > mean(fine_arts)

## 6. Comparing Single Values Against Vectors ##

gpa <- mean(final_scores)
above_average <- (gpa < final_scores)

## 7. Logical Indexing ##

gpa <- mean(final_scores)
above_average <- (gpa < final_scores)
best_grades <- final_scores[above_average]

## 8. Performing Arithmetic with Vectors ##

tests <- c(76, 89, 78, 88, 79, 93, 89)
homework <- c(85, 90, 88, 79, 88, 95, 74)
projects <- c(77, 93, 87, 90, 77, 82, 80)
johnny_scores <- (tests + homework + projects)/3
mean(johnny_scores)

## 9. Vector Recycling ##

tests <- c(76, 89, 78)
homework <- c(85, 90, 88, 79, 88, 95, 74)
projects <- c(77, 93, 87, 90, 77, 82, 80)
recycling <- tests + homework + projects

## 10. Appending Elements To A Vector ##

tests <- c(76, 89, 78)
homework <- c(85, 90, 88, 79, 88, 95, 74)
projects <- c(77, 93, 87, 90, 77, 82, 80)

class_names <- c("math", "chemistry", "writing", "art", "history", "music", "physical_education")
tests <- c(tests, 88, 79, 93, 89)
kate_grades <- (tests + homework + projects)/3

names(kate_grades) <- class_names

kate_gpa <- mean(kate_grades)

lower_than_GPA <- kate_grades < kate_gpa
kate_low_grades <- kate_grades[lower_than_GPA]