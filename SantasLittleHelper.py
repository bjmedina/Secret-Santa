'''
Bryan Medina
Santas Little Helper:
This helps assign people to their secret santa, then sends their secret
santa an email with their letter.
'''
from random import *
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage

def sendSantaLetter(santa, elf):
    ''' 
    Sends santa an email
    '''
    mailto = santa
    filename = elf + ".txt"
    
    file = open(filename, "r")
    msg = ""
    for line in file:
        msg = msg + line
        
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(gmailaddress , gmailpassword)
        mailServer.sendmail(gmailaddress, mailto , msg)
        print(" \n Sent!")
        mailServer.quit()

def get_contact_info(filename):
    '''File format should be:
    =========================
    <Name> <email@something.something>
    =========================
    
    This function reads the file, and creates a list of tuples.
    Each tuple is ["name", "email"].
    '''
    
    info = []
    
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            info.append( [a_contact.split()[0], a_contact.split()[1]] )
    
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

def badMatch(santa, chosen):
    '''
    We don't want some pairs (i.e we don't want couples to get each other).
    Let's not make those happen.
    '''
    
    goodToGo = True
    
    if( santa is "Ashley" and chosen is "Dylan"):
        goodToGo = False
    elif( santa is "Dylan" and chosen is "Ashley"):
        goodToGo = False
    elif( santa is "Nathan" and chosen is "Lori"):
        goodToGo = False
    elif( santa is "Lori" and chosen is "Nathan"):
        goodToGo = False
    elif( santa is "Bryan" and chosen is "Minh"):
        goodToGo = False
    elif( santa is chosen ):
        goodToGo = False

    return goodToGo


''' 
Fun begins here
Getting the data set up the way we want it to be
'''

filename = "text.txt"

# Get the contact info
info = get_contact_info(filename)

# We need to generate the pairs now
pairs = [ [person[0], " "] for person in info ]
shuffle(pairs)

chosen = [ elf[0] for elf in info ]

for santa in pairs:
    
    r_c = randint(0, len(chosen)-1)
    
    while( not badMatch(santa[0], chosen[r_c]) ):
        r_c = randint(0,len(chosen))
        
    santa[1] = chosen[r_c]
    del chosen[r_c]

for pair in pairs:
    pair[0] = getEmail(pair[0], info)
    print(pair)

cont = input("Would you like to continue?\n")


if cont is "Yes":

    '''
    Time to send the email
    '''
    import smtplib

    gmailaddress = "itsfuknsantaclaus@gmail.com"
    gmailpassword = "quesO??1"
    
    
    def sendSantaLetter(santa, elf):
        
        mailto = santa
        filename = elf + ".txt"
        
        file = open(filename, "r")
        msg = ""
        for line in file:
            msg = msg + line
            
            mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
            mailServer.starttls()
            mailServer.login(gmailaddress , gmailpassword)
            mailServer.sendmail(gmailaddress, mailto , msg)
            print(" \n Sent!")
            mailServer.quit()
            
    for pair in pairs:
        sendSantaLetter(pair[0], pair[1])
                
