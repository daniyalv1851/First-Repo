class Human:
    population = 0
    details = []
    deceased = []
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.split_name = addName.split(" ")
        self.raw_name = self.split_name[0] + "_" + self.split_name[1]
        Human.population += 1
        Human.details.append([self.name, self.dob])
    """ def die(self, dod):
        self.dod = dod
        Human.population -= 1
        for i in range(len(Human.details)):
            if Human.details[i - 1] == self.raw_name:
                Human.deceased.append([Human.details[i - 1], self.dod])
                del Human.details[i - 1]
    """

    @classmethod
    def getPop(cls):
        return Human.population
    @classmethod
    def getDetails(cls):
        return Human.details
    @classmethod
    def getDeceased(cls):
        return Human.deceased
    def die(dead, dod):
        for person in range(len(Human.details)):
            print("I am running!!" + str(person))
            checkArray = Human.details[person]
            if checkArray[0] == dead:
                Human.deceased.append([Human.details[person], dod])
                del Human.details[person - 1]


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
        killName = input("Enter name of deceased.")
        killDod = input("Enter date of death. Format: DD/MM/YY")
        # name_to_kill = killName.split(" ")
        # finalKillName = name_to_kill[0] + "_" + name_to_kill[1]
        Human.die(dead = killName, dod = killDod)
    elif command == "deceased":
        print(Human.getDeceased())
    elif command == "end":
        isLooping = False

