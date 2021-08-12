import sys

adj = input("Write an adjective: ")
adj2 = input("Write an adjective: ")
brd = input("Name a bird: ")
rom = input("name a room: ")
ptv = input("name a past tense verb: ")
vrb = input("name a verb: ")
rel = input("name a family member: ")
non = input("Write a noun: ")
lqd = input("Name a liquid: ")
vng = input("Name an ing verb: ")
pbp = input("name a part of the body: ")
pln = input("name a plural noun: ")
vng2 = input("name an ing verb: ")
non2 = input("write a noun: ")
madLib = "It was a "+ adj +", cold November day. I woke up to the "+ adj2 +" smell of"+ brd +"roasting in the "+ rom +" downstairs. I "+ ptv +" down the stairs to see if I could help "+ vrb + " the dinner. My Mom said, 'See if "+ rel +" needs a fresh "+ non +".' So I carried a tray of glasses full of "+ lqd +" into the "+ vng +" room. When I got there, I couldn't believe my "+ pbp +"! There were "+ pln +" "+ vng +" on the "+ non2+"!"
print("Welcome to PyLibs!")

print(madLib)

words = madLib.split(" ")

for x in words: 
    print(x)
    