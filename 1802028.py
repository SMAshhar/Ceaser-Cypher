######################################################################
##########################  MAIN MENU ################################
######################################################################

def menu():
    print( """
        ### Main Menu ###

        1. Encrypt a text
        2. Decrypt a text
        3. Exit
    """)


    choice = input("Please select a number: ")

    if choice == '1' or choice == '2' or choice == '3':
        choice = int(choice)
    else:
        print('\n######## WRONG SELECTION ########')
        print('\nPlease select with a valid number.')
        menu()
    
    return choice

######################################################################
##########################  ENCRYPTION ###############################
######################################################################

###########################  READ FILE ###############################


def read_file():
    print('###################################')
    print('######### TEXT ENCRYPTED ##########')
    print('###################################')
    with open('plaintext.txt') as f:
        x =  f.read()
        
    return x


##########################  KEY CREATION #############################

def Key(DOB, SID, name):
    DIS = SID[::-1]                  # reversing SID
    Sum = int(DIS) + int(DOB)        # adding DOB and SID_rev
    Ans = Sum % len(name)            

    if Ans % 2 == 0:
        key = int(DIS) + len(name)
    else:
        key = len(name) + int(DOB)
    
    with open('Enc_key.txt', 'w') as f:
        f.write(str(key))
    return key
 
############################  AVERAGE  ###############################

def aveg(key):
    y = [int(x) for x in str(key)]
    return round(sum(y)/ len(str(key)))

#######################  SAVING ENCRYPTED  ###########################

def cypher(encrypted_data):
    with open("ciphertext.txt", 'w') as f:
        f.write(encrypted_data)

######################################################################
##########################  DECRYPTION  ##############################
######################################################################

###########################  READ FILE ###############################


def read_file1():
    print('###################################')
    print('######### TEXT DECRYPTED ##########')
    print('###################################')
    with open('ciphertext.txt') as f:
        x =  f.read()
        
    return x 

#########################  LOADING ENC_KEY ############################

def enc_key():
    with open("Enc_key.txt") as f:
        key = int(f.read())

    return key

#######################  SAVE DECRYPTED DATA ##########################

def decypher(decrypted_data):
    with open('Decrypted.txt', 'w') as f:
        f.write(decrypted_data)


######################################################################
#######################  MAIN ENC FUNCTION  ##########################
######################################################################


def encrypt():
    with open('Student_info.txt') as f:
        x =  f.readlines()
        DOB = x[0].rstrip('\n')
        SID = x[1].rstrip('\n')
        name = x[2]
    
    data = read_file()
    key = aveg(Key(DOB, SID, name))
    

    encrypted_data = ""
    for character in data:
        encrypted_data += chr(ord(character) + key)
    
    cypher(encrypted_data)

######################################################################
#####################  MAIN DECRYPT FUNCTION  ########################
######################################################################

def decrypt():

    data = read_file1()
    key = aveg(enc_key())

    decrypted_data = ""
    for character in data:
        decrypted_data += chr(ord(character) - key)

    decypher(decrypted_data)



######################################################################
#########################  MAIN FUNCTION  ############################
######################################################################

x = menu()

if x == 1:
    encrypt()

elif x == 2:
    decrypt()

elif x == 3:
    print('\nEXITING NOW ...!')


