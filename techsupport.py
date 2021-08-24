#Wow, you read source code? Help me by adding some code to Tech Support Simulator, testing it, then run the build task!
#Ensure you get the original, safe copy of this by getting it from the repository from GitHub. Typed GitHug on accident, but I would like GitHug better than GitHub.
from gtts import gTTS
from playsound import playsound
import os
import random
import time
def tts(mytext):
    language = "en"
    sound = gTTS(text=mytext, lang=language, slow=False)
    sound.save("temp.mp3")
    playsound("temp.mp3")
    os.remove("temp.mp3")
def phn():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]
mode = input("Type in Text or Phone.")
if mode == "Text":
    def tts(mytext):
        print(mytext)
tts("Welcome to Tech Support Simulator!")
tts("What is your name, and what do you want your company to be named?")
myname = input("Your name: ")
companyname = input("Company name: ")
tts("Your name is " + myname + " and you are working for " + companyname + ".")
tts("Now, here is what you would hear when you call " + companyname + ".")
tts("Thank you for calling " + companyname + " support. Please wait while we transfer you to a support representative.")
tts("Now, I cut out the music because that lasts for a WEEK.")
tts("Now, your job is to handle the phone calls.")
tts("Your email address is support@" + companyname + ".com")
tts("And you are recieving phone calls at " + phn() + ". To get the tech support, you can call " + phn() + ".")
tts("Now, " + companyname + " has a new great Python program!")
tts("The name of it is " + companyname + " Phone System!")
tts("Just call " + companyname + "'s phone, and you can get forwarded!")
tts("Now, type in python phone.py into your computer.")
cmdtest = input("N:\\Programs\\Python>")
while not cmdtest == "python phone.py":
    tts("Remember, you needed to type in python phone.py to get the phone receiver.")
    cmdtest = input("N:\\Programs\\Python>")
tts("Running Phone Reciever")
tts("Yay, you got the Phone Receiver set up!")
tts("Now, the phone reciever is a program you should run all the time. Whenever you get a call, it asks you whether you want to answer it.")
tts("Now, I will go back home.")
print("Phone Reciever")
print("Ready for calls")
time.sleep(9)
tts("You got a call.")
input("Type Y to accept, or N to decline.")
def call1():
        tts("This is a test of the Phone System.")
        tts("I will hang up now.")
call1()
tts("The Phone System worked!")
tts("Now, do you want to play sandbox mode or story mode?")
mode = input("Type in Story or Sandbox: ")
if mode == "Story":
    tts("Story mode")
elif mode == "Sandbox":
    tts("Sandbox mode")
else:
    tts("Remeber, there is a capital S in Story or Sandbox mode.")
tts("A call was just ended.")
print("Phone Reciever")
print("Ready for calls")
time.sleep(7)
tts("You got a call.")
input("Type Y to accept, or N to decline.")
tts("Hi!")
tts("I need help with my iPad.")
tts("Do you offer help with iPads?")
command = input("You: ")
if command == "Yes." or "Yes!":
    tts("OK!")
else:
    tts("Exiting out of Tech Support Simulator.")
    exit()
tts("Now, whenever I turn it on, my iPad gives me a notifaction saying I need to do something with my phone number.")
tts("How do you get rid of it?")
command = input("You: ")
score = 0
yelpreviews = []
yelp = 0
if command == "Click on it!" or "Click on it.":
    tts("OK, I clicked on it.")
    tts("Should I say yes or no?")
    command2 = input("You: ")
    if command2 == "Yes!" or command2 == "Yes.":
        tts("Thank you!")
        score = score + 6
    elif command2 == "No." or command2 == "No!":
        tts("It now wants me to change my phone number!")
        score = score - 2
        tts("I really wish I just said yes.")
elif command == "I need to remotly acess your iPad.":
    print("This isn't the place to try out your tech support scammer skills.")
else:
    print("That solution is not in Tech Support Simulator.")
tts("Your current score is " + str(score) + "!")
print("Phone Reciever")
print("Ready for calls")
if score < 1 and mode == "Sandbox":
    tts("Sorry, but if you don't have any points by your 3rd call, I will have to fire you.")
    tts("If you didn't expect that, then maybe read your contract before working here at " + companyname + ".")
    tts("And that was the easiest Tech Support Job yet!")
    tts("That happens to me ever year, and I click yes and nothing happens!")
    tts("Hope you do better!")
time.sleep(6)
tts("You got a call.")
input("Type Y to accept, or N to decline.")
tts("Hi!")
tts("I need help with my Chromebook.")
tts("Whenever I right click any link, I have the option to open it in Copy to clipboard.")
tts("COPY TO CLIPBOARD!!")
tts("Could you help me get that off my Chromebook?")
command = input("You: ")
if command == "Powerwash your Chromebook!" or command == "Powerwash your Chromebook." or command == "Powerwash it!" or command == "Powerwash it.":
    tts("What does powerwash mean, and what does it do?")
    input("You: ")
    tts("OK, got it.")
    tts("But I have files stored in my downloads folder, which a powerwash deletes!")
    command = input("You: ")
    if command == "Back them up to Google Drive!" or command == "Back them up to Google Drive." or command == "Back up your files." or command == "Back up your files!" or command == "Back up your files to Google Drive!" or command == "Back up your files to Google Drive.":
        tts("I don't understand why I didn't do that before!")
        tts("Now powerwashing!")
        #time.sleep(random.randint(120, 340))
        time.sleep(1)
        tts("Done powerwashing and setted up my Chromebook!")
        tts("And it has gone away!")
        tts("Thank you!")
        tts("I'm going to reccomend you to my family!")
        print("The tech support I got from " + companyname + " was great!")
        print("If you want great tech support, ask " + myname + " the Expert!")
        tts("Bye!")
        score = score +  12
        #OSFirstTimer reference, for all you OSFirstTimer viewers
    elif command == "Click on it!" or command == "Click on it.":
        tts("It just copied the link to my clipboard.")
        tts("I'm going to call another tech support company!")
        score = score - 9
tts("You have " + str(score) + " points.")
print("Phone Reciever")
print("Ready for calls")
time.sleep(5)
tts("Phone Reciever got an update!")
tts("You can now see what the person needs help with before you answer your call!")
tts("You got a call!")
print("This person needs help with coding together using Git.")
input("Type Y to accept, or N to decline.")
tts("Hi!")
tts("I need help with command line Git.")
tts("I want to collabrate with my friends on coding!")
tts("I installed Git through WinGet.")
print("The Windows Package Manager (also known as winget) is a free and open-source package manager designed by Microsoft for Windows 10 and Windows 11. It consists of a command-line utility and a set of services for installing applications. ISVs can use it as a distribution channel for their software packages.")
print("https://en.wikipedia.org/wiki/Windows_Package_Manager")
tts("Now how am I supposted to git up and running?")
command = input("You: ")
if command == "Open up your terminal!" or command == "Open up your terminal.":
    time.sleep(5)
    tts("OK, got my terminal open.")
    tts("What should I type in?")
    print("Windows PowerShell")
    print("Copyright (C) Microsoft Corporation. All rights reserved.")
    print("")
    print("Try the new cross-platform PowerShell https://aka.ms/pscore6")
    mstommy = input("PS C:\\Users\\Me> ")
    if mstommy == "git clone":
        tts("Ummm, you just made a mistake.")
        tts("You make a repository on GitHub online, and then install GitHub CLI, and then install Git for Windows, and then run git clone https://github.com/GithubUsername/dtest.git. To keep it updated, you can use git push and git pull.")
        score = score - 6
    if mstommy == "You don't need to be here.":
        tts("OK. Where to go?")
        command = input("You: ")
        if command == "To GitHub!":
            tts("OK.")
            tts("Just created my GitHub account a couple of days ago!")
            tts("Now what do I do here?")
            command = input("You: ")
            if command == "Create a repository!" or command == "Create a repository.":
                tts("I created a private repository!")
                tts("Now how do I get this on Git?")
                command = input("You: ")
                if command == "Run a command!" or command == "Run a command.":
                    tts("What command?")
                    input("PS C:\\Users\\Me\\Coding")
                    if command == "git clone":
                        tts("Assume I put a Git URL here.")
                        time.sleep(5)
                        tts("My completed command is git clone https://github.com/Me/MyNewGame.git!")
                        tts("Now I am going to run that!")
                        print("Running command...")
                        time.sleep(2)
                        print("Thank you!")
                        score = score + 9
print("Your new score is " + str(score) + "!")