import os

user=input("Enter the img name:\n")

os.system('fswebcam '+user)

if(user):

    print("Image is Captured")
else:
    print("ERROR because file is already exist")