'''
Bryan Medina
Santas Little Helper:
This helps assign people to their secret santa, then sends their secret
santa an email with their letter.
'''
from random import *
import smtplib

# Super sensitive information
gmailaddress = "itsfuknsantaclaus@gmail.com"
gmailpassword = "a password that is not the password to that email"

SUBJECT = "You've received a letter!"

def sendSantaLetters(picks, info):
    
    for i in range(0, len(picks)):
        email = getEmail(picks[i], info)
        good_person = picks[ (i+1)%(len(picks)) ]
        
        sendSantaLetter(email, good_person)
        
        print(str(i+1) + " out of " + str(len(picks)) + " sent")
                    
def sendSantaLetter(santa, elf):
    ''' 
    Sends santa an email
    '''
    mailto = santa
    filename = elf + ".txt"
    
    file = open(filename, "r")
    msg = ""
    
    with open(filename, mode='r') as file_of_stuff:
        for line in file_of_stuff:
            msg = msg + line

        
    message = 'Subject: {}\n\n{}'.format(SUBJECT, msg)
    
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , message)
    mailServer.quit()

def get_info(filename):
    '''File format should be:
    =========================
    <something> <something>
    
    e.g.
    <Name> <email@something.something>
    or
    <Name> <Name>
    =========================
    
    This function reads the file, and creates a list of tuples.
    Each tuple is [something, something].
    List is [ [something, something], [something, something], ... ]
    '''
    
    info = []
    
    with open(filename, mode='r') as file_of_stuff:
        for something in file_of_stuff:
            info.append( [something.split()[0], something.split()[1]] )
    
    return info
    
def getEmail(santa, info):
    '''
    This just finds the email of the specified person
    '''

    email = ""
    
    for emails in info:
        if(emails[0] is santa):
            email = emails[1]
            break

    return email

def badMatch(santa, chosen, avoid):
    '''
    We dont want some pairs (i.e we dont want couples to get each other).
    Lets not make those happen.
    '''

    goodToGo = True

    for pair in avoid:
        if(santa == pair[0] and chosen == pair[1]):
            goodToGo = False

        if(santa == pair[1] and chosen == pair[0]):
            goodToGo = False
    
    if(santa == chosen):
        goodToGo = False
        
    return goodToGo

def check(picks, avoid):
    '''
    Check to see if there are any bad matches...
    '''
    
    all_good = True

    for i in range(0, len(picks)):
        santa = picks[i]
        choice = picks[ (i+1)%(len(picks)) ]
        if( not badMatch(santa, choice, avoid) ):
            return False

    return all_good

''' 
Fun begins here
Getting the data set up the way we want it to be
'''

# file with everyone's name and info
filename = "emails.txt"
avoid    = "avoid.txt"

# Get the contact info
info = get_info(filename)
bad_matches = get_info(avoid)

# get names
picks = [ person[0] for person in info ]
shuffle(picks)

# make sure this is a good choice for picks
while( not check(picks, bad_matches) ):
    shuffle(picks)

# time to send letters!
sendSantaLetters(picks, info)




