# madLib generator using a dictionary              emtn = emotion   actn = action
import sys



class MadLibs :

    def __init__(self, title , madLibs):
        
        self.title = title
        self.madLibs = madLib

    def play(): 
        adj    = input("Write an adjective: ")
        noun   = input("Write a noun: ")
        vng    = input("Name an ing verb: ")
        emtn   = input("name an emotion: ")
        actn   = input("name an action: ")
        friend = input("name an friend: ")

        print(MadLibs.title)

        for words in MadLibs.madLibs:
            print(words)


madLib = (
    "One Valentine's "+ noun +" I was "+ vng +", when I looked in my "+ noun +" and saw a "+ adj +" "+ noun +" !"
    "It said, 'Will you be my "+ noun +"?' I was so "+ emtn +"! I "+ actn +" to see who it was from, but there was"
    "no "+ noun +". So, at "+ noun +", I asked for clues, but "+ friend +" didn't know about it. Finally, someone"
    "told me that "+ friend +" gave me the "+ noun +"."
)

m1 = MadLibs("Thanks Giving Giggle", madLib)

m1.play()

