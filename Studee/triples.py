class Member:
    Gender = "Female" # Class Variable
    def __init__(self, name, s_Num, age, birthday, rep_Color):
        self.name = name           #Instance Variable   
        self.s_Num = s_Num         #Instance Variable
        self.age = age             #Instance Variable
        self.birthday = birthday   #Instance Variable
        self.rep_Color = rep_Color #Instance Variable

    def gnd_Part(self, part):
        print(self.name + " part is: " + part)
    