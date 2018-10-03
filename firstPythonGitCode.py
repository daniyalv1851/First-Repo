class Human:
    population = 0
    details = []
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.split_name = addName.split(" ")
        self.raw_name = self.split_name[0] + "_" + self.split_name[1]
        Human.population += 1
        Human.details.append([self.name, self.dob])
    def die(self):
        Human.population -= 1
        for i in range(len(Human.details)):

            if Human.details[i] == self.raw_name:
                del(Human.details[i])


    @classmethod
    def getPop(cls):
        return Human.population
    @classmethod
    def getDetails(cls):
        return Human.details

aryan = Human("Aryan Kinge", "09/11/01")

isLooping = True

while isLooping:
    command = input('Enter Command.')
    if command == "add":
        addName = input("Enter Name.")
        addDob = input("Add DOB. Format: DD/MM/YY")
        name_to_add = addName.split(" ")
        finalName = name_to_add[0] + "_" + name_to_add[1]
        exec(finalName + " = Human(addName, addDob)")
    elif command == "details":
        print(Human.getDetails())
    elif command == "kill":
        killName = 1
    elif command == "end":
        isLooping = False
