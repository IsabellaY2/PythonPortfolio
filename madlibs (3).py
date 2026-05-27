
#Isabella Yan
import random

def madlibs():
    walking= input ("Name an animal. ")
    if walking == "random":
        animal = ["dog", "cat", "pig", "sheep", "horse"]
        walking = random.choice (animal)

    monster = input ("Name another animal. ")
    if monster == "random":
        creep= ["dragon", "spider", "vampire", "ghost"]
        monster = random.choice (creep)

    place = input ("Name a place. ")
    if place == "random":
        area = ["Diner", "small cafe", "Janitor's closet", "Abandoned warehouse"]
        place = random.choice (area)

    sound = input ("Name a sound. ")
    if sound == "random":
        noise = ["honk", "beep", "growl"]
        sound = random.choice (noise)

    print (f"""I was walking with my  \033[1m{walking.upper()}\033[0m until a saw a big creepy \033[1m{monster.upper()}\033
           started chasing us. We decided to hide in the \033[1m{place.upper()}\033[0m
           until we heard a soft but loud \033[1m{sound.upper()}\033[0m brushing next to us""")


#main
madlibs()
