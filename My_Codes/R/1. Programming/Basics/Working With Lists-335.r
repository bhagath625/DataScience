## 1. Lists: Objects That Can Contain Multiple Data Types ##

uni_clubs <- list("ballroom dancing","rugby","bird watching", "pottery")

## 2. Anatomy of a List ##

club_title <- c("Chess Club")
club_description <- c("Meets two nights a week for members to play chess. Snacks are provided.")
club_dues <- c(50, 20, 15)
meeting_days <- c("Monday", "Wednesday")
meeting_times <- c("6:00 pm", "8:00 pm")
club_meetings <- rbind(meeting_days, meeting_times)
chess_club <- list(club_title, club_description, club_dues, club_meetings)

## 3. Assigning Names to List Objects ##

chess_club_names <- c("club_title", "club_description", "club_dues", "club_meetings")
# Type your code below
names(chess_club) <- chess_club_names

## 4. Indexing Lists ##

chess_club[[c(3,2)]]

## 5. Modifying List Elements ##

chess_club[[c(3, 3)]] <- 5
chess_club[[c(3, 3)]]

## 6. Adding Elements to Lists ##

first_years <- c(12, 15)
names(first_years) <- c("spring", "fall")
chess_club[["first_years"]] <- first_years
chess_club$first_years[[2]]

## 7. Combining Lists ##

uni_clubs <- list(rugby_club = rugby_club, ballroom_dancing = ballroom_dancing, chess_club = chess_club)