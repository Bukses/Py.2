import random
import string
#to collect details from user.
def details():
    first_name=(input("Enter First Name: \n"))
    last_name=(input("Enter Last Name: \n"))
    email=(input("Enter Email Address: \n"))
    details=(first_name, last_name, email)
    return details
#to generate a random password for user.
def gen_password(details):
    characters= string.ascii_lowercase
    length=5
    random_password="".join(random.choice(characters) for i in range(length))
    password=str(details[0][0:2] + random_password + details[1][-2:])
    return password

status=True
container={} #to collect all details from user including password
while status:
    user_details=details()
    password=gen_password(details)
    print("Your password is: " + str(password)) #this shows the generated password
    #check if user likes the generated password
    password_like=input(str("Do you want to save this password? Kindly enter Yes or No"))
    password_loop=True
    while password_loop:
        if password_like== "Yes":
            details.append(password) #this is to add the password to the details if user likes it
            container.append(details)  #this is to add all the details to the container

            password_loop=False  #user is prompted to enter another password not less than 9 characters
        else:
            user_password=input(str("Enter password not less than 9 characters"))
            password_len=True
            while password_len:
                if len(user_password)>=9:
                    details.append(user_password) #to add the newly generated password to details
                    container.append(details)
                    password_len=False
                    password_loop=False
                else:
                    print("Your password is less than 9 characters")
                    user_password=input(str("Enter password not less than 9 characters"))
     #to enter new details for another user, the process may begin all over again or end depending on the selection of the user
    new_user=input(str("Would you like to enter new details? Kindly enter Yes or No"))
    if new_user=="No":
        status=False
        for item in container:
            print(item)
    else:
        status=True





  