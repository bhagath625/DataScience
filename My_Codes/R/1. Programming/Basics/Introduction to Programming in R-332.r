## 2. Programming in R ##

125 - 3

## 3. R Syntax Rules ##

224 + 667
35 / 7
(22 * 5) +3

## 4. Exploring Data With R ##

(92 + 87 + 85) / 3 # math
(90 + 81 + 92) / 3 # chemistry
(84 + 95 + 79) / 3 # writing
(95 + 86 + 93) / 3 # art
(77 + 85 + 90) / 3 # history
(92 + 90 + 91) / 3 # music
(85 + 88 + 95) / 3 # physical education

## 5. Assigning Values to Variables ##

math <- 88
chemistry <- 87.66667
writing <-  86
art <- 91.33333
history <- 84
music <- 91
physical_education <- 89.33333

## 6. Programming With Variables ##

math <- 88 
chemistry <- 87.66667
writing <-  86
art <- 91.33333
history <- 84
music <- 91
physical_education <- 89.33333
gpa <- (math + chemistry + writing + art + history + music + physical_education)/7

## 7. Vectors: Storage for Multiple Values ##

math <- 88 
chemistry <- 87.66667
writing <- 86
art <- 91.33333
history <- 84
music <- 91
physical_education <- 89.33333
final_scores <- c(math, chemistry, writing, art, history, music, physical_education)

## 8. Efficient Programming with Functions and Vectors ##

final_scores <- c(math, chemistry, writing, art, history, music, physical_education)
gpa <- mean(final_scores)

## 9. Practice with Functions and Vectors ##

final_scores <- c(math, chemistry, writing, art, history, music, physical_education)
max(final_scores)
min(final_scores)
length(final_scores)