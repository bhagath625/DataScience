## 1. Introduction to Remote Repositories ##

/home/dq$ git clone /dataquest/user/git/chatbot

## 2. Making Changes to Cloned Repositories ##

/home/dq$ cd /home/dq/chatbot

## 3. Overview of the Master Branch ##

/home/dq/chatbot$ git branch

## 4. Pushing Changes to the Remote ##

/home/dq/chatbot$ git push origin master

## 5. Viewing Individual Commits ##

/home/dq/chatbot$ cd /home/dq/chatbot

## 6. Commits and the Working Directory ##

/home/dq/chatbot$ git --no-pager diff $HASH2 $HASH

## 7. Switching to a Specific Commit ##

/home/dq/chatbot$ HASH='git rev-list --max-parents=0 HEAD'

## 8. Pulling From a Remote Repo ##

/home/dq/chatbot$ git pull

## 9. Referring to the Most Recent Commit ##

/home/dq/chatbot$ git resey --hard HEAD~1