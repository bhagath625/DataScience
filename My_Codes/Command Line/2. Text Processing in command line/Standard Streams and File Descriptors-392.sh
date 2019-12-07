## 1. Standard Streams ##

/home/dq$ ls /home/inexistent 2>>stderr

## 3. Redirecting Two Streams ##

/home/dq$ ls /dev/null /home/inexistent >all-output 2>all_output

## 6. Duplicating File Descriptors ##

/home/dq$ ls /dev/null /home/inexistent >all_output_v2 2>&1

## 7. Order of Redirections ##

/home/dq$ ls /dev/null /home/inexistent 2>&1 1>redirection_order

## 8. Standard Input ##

/home/dq$ cat sorted_stdin

## 9. Redirecting Standard Input ##

/home/dq$ tr [:lower:] [:upper:] <sorted_stdin