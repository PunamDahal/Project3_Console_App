# -----------Welcome Intro----------

import os
from turtle import clear

def restart_program():
    restart = input("Would you like to restart this program?(y/n)")
    if restart == "yes" or restart == "y":
        console_app()
    if restart == "n" or restart == "no":
        print( "Program terminating...")

def console_app():

    print(""" 'User Management System' \n 
    Tasks to Do: \n
    1.User Info Creation
    2.User Listing
    3.User Info Editing
    4.User Info Deleting""")

    #-------------TASKS--------------#

    try:
        global userInput
        userInput = int(input('\n Choose a number from above list:'))

    except:
        ('\n Invalid Option! Enter a valid number!!')

    finally:
        ('\n')
    
    # -----------FILE HANDLING LOOP-----------#
        if(userInput == 1):
            print("\nUSER INFO CREATION!!!\n")
            # -----------USER INFO CREATION-----------#
        
            global fileName
            fileName = input("Enter a name for new file: ")
            global f
            with open(fileName,'x') as f:
                    f.write('\nUser Information\n')
                    f.write('\nFullName\t\tBirthDate\t\tAddress\n')
                    n= int(input('Enter the number of user data you want to enter:'))
                    for i in range(n) :
                        name = (input('Enter FullName:'))
                        birthDate = (input('Enter birthdate (yyyy/mm/dd): '))
                        address= (input('Enter Address: '))
                        f.write(name )
                        f.write('\t\t')
                        f.write(birthDate)
                        f.write('\t\t')
                        f.write(address)
                        f.write('\n')
            f.close()

            console_app()
        # -----------USER LISTING-----------#


        elif(userInput == 2):
            print('\nUSER LISTING\n')
            f = open(fileName, "r")
            for name in f:
                print("{}".format(name))
        
            f.close()
            console_app()


        # -----------USER INFO EDITING-----------#


        elif(userInput == 3):
            print('\nUSER INFO EDITING\n')
            print("""1. EDIT FILE
                    2. ADD TO FILE""")
            choose= int(input('Choose 1 or 2:'))
            if(choose == 1):
                try:
                    f = open(fileName,'w')
                    name = (input('Enter FullName:'))
                    birthDate = (input('Enter birthdate (yyyy/mm/dd): '))
                    address= (input('Enter Address: '))
                    f.write(name )
                    f.write('\t\t')
                    f.write(birthDate)
                    f.write('\t\t')
                    f.write(address)
                    f.write('\n')

                except:
                    print("Oops! something error")
                    restart_program()

            elif(choose==2):
                            f=open(fileName,'a')
                            name = (input('Enter FullName:'))
                            birthDate = (input('Enter birthdate (yyyy/mm/dd): '))
                            address= (input('Enter Address: '))
                            f.write(name )
                            f.write('\t\t')
                            f.write(birthDate)
                            f.write('\t\t')
                            f.write(address)
                            f.write('\n')

            else:
                    print('Error! Choose a valid option.')
                    restart_program()
                
            f.close()
            console_app()

        # -----------USER INFO DELETING-----------#


        elif(userInput == 4):
            print('USER INFO DELETING')
            print("""1. DELETE DATA
                    2. DELETE FILE""")
            choose= int(input('Choose 1 or 2:'))
            if(choose == 1):
                try:
                    with open(fileName, 'r') as f:
                        line = f.readlines()
                    global fileName_2
                    fileName_2=input('enter a new file name:')

                    with open(fileName_2, 'w') as fw:
                        data=input('Enter the text to be deleted:')
                        for line in data:
                            if line.strip('\n') != data:
                                fw.write(line)
                        print("Deleted")
                        fw.close()
                    
                    with open(fileName_2, 'r') as fw:
                        for name in fw:
                            print("{}".format(name))

                except:
                    print("Oops! something error")
                    restart_program()

            elif(choose==2):
                    os.remove(fileName)

            else:
                    print('Error! Choose a valid option.')
                    restart_program()
                
            f.close()
            console_app()

# -------------PROGRAM INVALID----------

        elif(userInput < 0 or userInput > 4):
            print(' Invalid Option! Enter a valid number!')
            restart_program()

        f.close()
       
console_app()



        


