#Fernando Guzman
#03/09/25

##Using the already working code, answer questions and adjust code to instructions

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses
        
    def get_nickname(self):
        return self.nickname
    def get_weapons(self):
        return self.weapons
    def get_weaknesses(self):
        return self. weaknesses
    def profile(self):
        return self.nickname, self.weapons, self. weaknesses

def taskAbility(taskItems, taskDebuff):
    return all(item in player1.weapons for item in taskItems) and not any(debuff in player1.weaknesses for debuff in taskDebuff)
    
player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

task1Items = ['rope', 'coat', 'first aid kit']
task1Debuff = ['slow']

task2Items = ['pan', 'groceries']
task2Debuff = ['small']

task3Items = ['pen', 'paper', 'idea']
task3Debuff = ['confusion']

for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

def taskChoice():
    while True:
        userChoice = input("""Please select from the following tasks:
'climb mountain', 'cook meal', or 'write book' """).strip().lower()

        if userChoice == 'climb mountain':
            return task1Items, task1Debuff
        elif userChoice == 'cook meal':
            return task2Items, task2Debuff
        elif userChoice == 'write book':
            return task3Items, task3Debuff
        else:
            print("Invalid input. Please try again. ")

task_items, task_debuff = taskChoice()
                  
if taskAbility(task_items, task_debuff):
    print(player1.nickname + " is able to do task.")
else:
    print(player1.nickname + " is unable to do task.")
