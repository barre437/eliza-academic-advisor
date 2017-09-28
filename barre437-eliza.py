#!/usr/bin/python

#import regex library
import re

#var that holds user input
response = ''

#user's name
name = ""
major = ""
home = ""

#Regex's to be searched for. Many are keyword identification.
#Others are looking for sequences of words to make tranformations.
greetRE = re.compile(r'\b[Hh]i|[Hh]ello|[Hh]ey\b')
failRE = re.compile(r'\bfail.?')
sleepRE = re.compile(r'\btired|sleep.?|slept|exhausted\b')
stressRE = re.compile(r'\bstress|pressure|overwhelm.?\b')
tutorRE = re.compile(r'\btutor.*\b')
registerRE = re.compile(r'\bregister.?|registration\b')
youmeRE = re.compile(r'(?s).*?([Yy]ou) (\w+) me (\w+)')
thisisRE = re.compile(r'(?s).*?[Tt]his is (\w+)')
howRE = re.compile(r'(?s).*?([Hh]ow) (\w+) [Ii] (\w+)')
idkRE = re.compile(r'(?s).*?[Ii] don\'*t know( \w+ )')
counselRE = re.compile(r'\bcounsel.?')
planRE = re.compile(r'\bplan.?')
creditRE = re.compile(r'\bcredit.?')
studyRE = re.compile(r'\bstudy.?')
readRE = re.compile(r'\bread.?')
writeRE = re.compile(r'\bwrit(e|i).?')
paperRE = re.compile(r'\bpaper.?')
robotRE = re.compile(r'\brobot.?')
youareRE = re.compile(r'(?s).*?([Yy]ou) are (\w+)')
#Dictionary that matches regex keys to function values.
reDict = {greetRE : "greetings", failRE : "fail", sleepRE : "sleep", stressRE : "stress", tutorRE : "tutor"
        , registerRE : "register", youmeRE : "youmeTransform", thisisRE : "thisis", howRE : "how", idkRE : "idk"
        , counselRE : "counsel" , planRE : "plan", creditRE : "credit", studyRE : "study", readRE : "read"
        , writeRE : "write", paperRE : "paper", robotRE : "robot", youareRE : "youare"}

#If more than one regex is matched in a response, the first will be stored
#the last will be executed immediately.
#If the next response doesn't have a matching regex, it will pop the first
#topic from the previous response
topicStack = []

#Regex functions. Keywords have a standard output. Others looking for sequences have transformations.
def direct(r):
        print "[eliza] Tell me more " + name + "."

def youare(r):
    print youareRE.sub(r'[eliza] Why do you say I am \2', r)

def robot(r):
    print "[eliza] Well now that's just ridiculous " + name + ", let's please move on."

def paper(r):
    print "[eliza] Papers tend to make up a large percentage of grades, so make sure you do well on them."

def write(r):
    print "[eliza] The writing center is a good place to get help writing papers."

def read(r):
    print "[eliza] Most people who fail classes ignore the readings."

def study(r):
    print "[eliza] It's important to cultivate good study habits."

def credit(r):
    print "[eliza] You need to take 15 credits a semester to graduate on time with 120 credits."

def plan(r):
    print "[eliza] Good planning and time management is key to success in college!"

def counsel(r):
    print "[eliza] You should definitely seek out counseling or therapy if you feel you need it " + name + "."

# Looks for I don't know, returns that they should know about what they don't know about.
def idk(r):
    t = idkRE.sub(r'[eliza] Well a student your age should know about\1', r)
    print t

# Looks for How _ I _, asks them how they think they find out about that.
def how(r):
    t = howRE.sub(r'[eliza] How do you think you find out about how you \3', r)
    print t

# Looks for this is _, asks them why they think this is _
def thisis(r):
    t = thisisRE.sub(r'[eliza] Why do you think this is \1?', r)
    print t

# Looks for you 1 me 2, asks why they say I 1 you 2
def youmeTransform(r):
    t = youmeRE.sub(r'[eliza] Why do you say I \2 you \3', r)
    print t

def register(r):
    print "[eliza] You should probably make sure you pass your current classes before registering for others! Let's just put that off for now " + name + "."

def tutor(r):
    print "[eliza] You should definitely get tutoring if you need academic help."

def stress(r):
    print (
    "[eliza] Have you tried utilizing a planner?\n[eliza] There's also help at the tutoring center for a lot of different subjects.\n[eliza] Otherwise, maybe you could try the counseling center if you're experiencing stress from more personal areas of your life.\n[eliza] Does any of that resonate with you " + name + ".")

def sleep(r):
    print "[eliza] Well, you should be getting more sleep " + name + ", at least 6 hours!"

def fail(r):
    print "[eliza] You're failing?! That's not good! Why are you failing?"

def greetings(r):
    print "[eliza] Um, yes we've already gone over greeting formalities, so let's just move forward? Maybe?"


# Outside while loop, initializes user name
print "[eliza] Hello, my name is Eliza the academic advisor, could you give me your name?"
name = raw_input(" ")
while len(name.split()) > 1:
    print "[eliza] I'm sorry, names are only 1 word! Please tell me just your first name!"
    name = raw_input(" ")
print "[eliza] " + name + "? Great, well, what's you major " + name + "?"
major = raw_input("[" + name + "] ")
print "[eliza] Do you like " + major + "?"
raw_input("["+name+"] ")
print "[eliza] Just one more question for my file, where are you from?"
home = raw_input("[" + name + "] ")
print "[eliza] Perfect. How can I help you today " + name + "?"


# main loop that runs until exit is typed
# Checks each user response to see if it matches any of the definied regexes
# Adds onto stack if they do.
# Pops top of the stack, runs associated function, and then takes in new input indefinitely
while response != "exit":
    # asks for input
    response = raw_input("[" + name + "] ")
    # checks for exit
    if response == "exit":
        break

    # checks for regex matches in user response
    for re, fn in reDict.items():
        m = re.search(response)
        if m:  # appends to stack if match is found
            topicStack.append(fn)

    # pops stack, or uses default tell me more
    try:
        locals()[topicStack.pop()](response)
    except IndexError:
        direct(response)
