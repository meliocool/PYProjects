question = input("are you husein? ")
age = int(input("How old are you? "))

if question.lower() == "no":
    print("You are correct, Husein is in another dimension called Mampang")
elif question.lower() == "yes":
    anotherQuestion = input("Okay, where do you live? ")
    if anotherQuestion.lower() == "mampang":
        print("You are correct, you are him")
    else:
        print("You are a fraud!")

if age < 18:
    minus = 18 - age
    print(f"You are wrong! you are {minus} years away from his true age")
elif age == 18:
    print("You have the same age as Hoosein")
else:
    print("You lowkey hitting unc status")

def reverseString(string):
    reverse = string[::-1]
    print(reverse)

reverseString("balls")