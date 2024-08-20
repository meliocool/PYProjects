# HOMIE NAMES USING **KWARGS
def homieName(**homie):
    print("Your Homie's name is", end=" ")
    for key,value in homie.items():
        print(value, end=" ")

firstName = input("What is your Homie's first name? ")
confirmation = input("Does your Homie have a middle name? ")
nameSections = {"First":firstName}
if confirmation == "Y":
    middleName = input("What is their middle name? ")
    nameSections["Middle"] = middleName
else:
    pass
lastName = input("What is their last name? ")
nameSections["Last"] = lastName
homieName(**nameSections)