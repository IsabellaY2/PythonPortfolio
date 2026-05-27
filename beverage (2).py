#Dataset of "Beverages Nutrition - Sheet1.csv" is taken from code.org
#Dataset Source:https://fdc.nal.usda.gov/
#Publisher: U.S. Department of Agriculture


#Purpose of Program: User inputs a response to specific questions in order to get an output of beverage(s) that specifically follows the user's requirements.


#initiative
import pandas as pd
import webbrowser
data=pd.read_csv('Beverages Nutrition - Sheet1.csv')
ID = data ['id'].tolist()	#analyze,clean, explore, and manipulate dataset
NAME = data ['Name'].tolist()
TYPE = data ['Type'].tolist()
sugar_free = data ['Sugar Free?'].tolist()
CAL = data ['Calories'].tolist()
FAT = data ['Fat (g)'].tolist()
PROTEIN = data ['Protein (g)'].tolist()
CARBS = data ['Carbohydrate (g)'].tolist()
SUGAR = data ['Sugars (g)'].tolist()
SODIUM = data ['Sodium (mg)'].tolist()
CAFFEINE = data ['Caffeine (mg)'].tolist()
WEIGHT = data ['Serving Weight (g)'].tolist()
DESCRIPTION = data ['Serving Description (fl oz)'].tolist()
CAL_WEIGHT = data ['200 Calorie Weight (g)'].tolist()
current=[]      #This is the starting filter
new=[]          #Where beverages that meets these standards are transferred temporarily
result=[]       #The final filter that will be printed out at the end


#function
def beverage ():
    kind_ask = input ("What type of drink would you like? ")
    kind = kind_ask.capitalize()
    for i in range(len(NAME)):
        if kind in TYPE[i]:
            current.append(i) #appends all beverages that is the type of drink the user has input.
    sweet (current) #This is to ensure that the computer will only check for the filtered beverages


def sweet (current):
    ask_sugar = input ("Type 'TRUE' for sugar-free and 'FALSE' for sugar: ")
    new = []        #another filter that is currently blank
    for i in current: #Only checks beverages that follow previous standards
        if str(sugar_free[i]).upper() == ask_sugar(): #force statement than boolean. Helped by my dad.
            new.append(i)  #Only adds beverages that suits this and its previous question
    amount = input("What is the maximum amount of calories would you like? ")
    cal(new, amount)


def cal (current, amount):      #Current is now the list from new. Similar structure as the function sweet.
    amount = float (amount)     #represents real numbers such as decimals.
    new = []        #Cleared out the new filter
    for i in current:
        if CAL[i] <= amount:    #If beverage's calories is less than or equal to amount
            new.append(i)       #only scans list that met previous requirements
    extra = input("What is the maximum amount of fat you would like? ")
    fat (new, extra)


def fat (current, extra):
    extra = float(extra)
    new = []
    for i in current:
        if FAT[i] <= extra:
            new.append (i)
    strength = input ("What is the minimum amount of proteins you would like? ")
    protein (new, strength)


def protein (current, strength):
    strength = float(strength)
    new = []
    for i in current:
        if PROTEIN[i] >= strength:  #If beverages' protein are greater or equal to "strength"
            new.append(i)
    carbs = input ("What is the maximum amount of carbs you would like? ")
    carbohydrate (new, carbs)


def carbohydrate (current, carbs):
    carbs = float(carbs)
    new = []
    for i in current:
        if CARBS[i] <= carbs:   #If beverages' carbohydrates are less than or equal to user’s input in "carbs"
            new.append(i)
    rush = input("What is the maximum amount of sugar you would like? ")
    sugar (new, rush)


def sugar (current, rush):
    rush = float(rush)
    new = []
    for i in current:
        if SUGAR[i] <= rush:
            new.append(i)
    salt = input("What is the maximum amount of sodium you would like? ")
    sodium(new, salt)


def sodium (current, salt):
    salt = float(salt)
    new = []
    for i in current:
        if SODIUM[i] <= salt:
            new.append(i)
    caf = input("What is the maximum amount of caffeine you would like? ")
    caffeine (new, caf)


def caffeine (current, caf):
    caf = float(caf)
    new = []
    for i in current:
        if CAFFEINE[i] <= caf:
            new.append(i)
    serving = input("What is the maximum serving weight you would like? ")
    weight (new, serving)


def weight (current, serving):
    serving = float(serving)
    new = []
    for i in current:
        if WEIGHT[i] <= serving:
            new.append(i)
    prescribe = input("What is the minimum amount of drink would you like in fl. oz? ")
    description (new, prescribe)


def description (current, prescribe):
    prescribe = float(prescribe)
    new = []
    for i in current:
        if prescribe <= DESCRIPTION[i]:
            new.append(i)
    weight_val = input("What is your maximum preferred calorie weight? ")
    calories (new, weight_val)


def calories (current, weight):
    weight = float(weight)
    result = []
    for i in current:
        if CAL_WEIGHT[i] <= weight:
            result.append(NAME[i])
    print (f"Beverages to try: {result}")       #This is the final code user will see.


#main
beverage()



