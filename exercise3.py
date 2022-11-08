# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, 
# they add a harmless Easter Egg to their program. Modify the program that prompts
#  the user for the file name so that it prints a funny message when the user types in 
#  the exact file name “na na boo boo”. The program should behave normally for all other
#   files which exist and don’t exist. Here is a sample execution of the program:

# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt

# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt

# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!
# We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.

#This code was written by Zackary Paulson
fname = input('Enter a file name: ') #created a file with whatever name specified by user
count = 0 #this is for the count to figure out how many lines of something are inside of a file

try: #this is my try loop to see if the file name is na na boo boo so the you have been punked message will appear
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d')
        exit()
    fopen = open(fname)
except FileNotFoundError:  #this escept catched whether or not the file exists or not 
    print('File cannot be opened: ',fname)
    exit()

for line in fopen: #this for and if sees how many lines that stbart with subject there are
        if line.startswith('subject:'): 
            count += 1

print('There were', count , 'subject lines  in', fname)
