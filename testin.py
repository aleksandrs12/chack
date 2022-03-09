import random


f = open("chuck.txt", "r")
f2 = open('newfile.txt', 'w')

f1 = f.read()


list = f1.split('.')

for n in range(len(list)):
    list[n] = list[n].strip()
print(list)

def add_joke(word):
    f2.write(replace_chack(word))

def replace_chack(word):
    return f1.replace('Chuck Norris', word)

def counting():
    return f1.count('doesnt')

def random_joke():
    global list
    print(list[random.randint(0, 14)])


vards = input('how do you want to replace Chuck Norris? ')
replace_chack(vards)
#print(f1)

add_joke(vards)
#print(counting())
random_joke()
f.close()