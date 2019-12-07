## 1. Introduction ##

/home/dq$ pwd

## 2. Create a Script ##

/home/dq$ echo -e 'import sys\n\nif __name__=="__main__":\n print(sys.argv[1])'

## 3. Change File Permissions ##

/home/dq$ chmod 0700 script.py

## 4. Create a Virtual Environment ##

/home/dq$ virtualenv -p /usr/bin/python3 script

## 5. Move the Script ##

/home/dq$ mv script.py printer

## 6. Execute the Script ##

/home/dq/printer$ python script.py "I'm so good at challenges!"