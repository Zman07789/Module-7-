#this code was made by zackary paulson
fhand = open('mbox-short.txt','r')
for line in fhand:                     
    dothing = line.rstrip().upper()       
    print(dothing)