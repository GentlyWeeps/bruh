import random
import winsound

class Wizard:     
    def __init__(self,dmg,hp,armor,item):
        self.dmg = dmg
        self.hp = hp
        self.armor = armor
        self.item = item
FireWizard = Wizard(140,40,50,"Basic Wand")
WaterWizard = Wizard(90,60,70,"Basic Wand")
AirWizard = Wizard(100,60,10,"Basic Wand")

class Fighter:
    def __init__(self,dmg,hp,armor,item):
        self.dmg = dmg
        self.hp = hp
        self.armor = armor
        self.item = item
RougeFighter = Fighter(30,200,50,"Fist")
MonkFighter = Fighter(100,100,0,"Fist")
BreserkerFighter = Fighter(40,200,0,"Fists")

def charSelect():
    global outcome
    global user
    global userClass
    global userstr
    outcome =""
    character = int(input("What type of character do you want to play as? \n 1: Ranged \n 2: Close Combat \n"))
    if character == 1:
        intselect = int(random.random()*10)
        userClass = "Wizard"
        if intselect%2 == 0:
            print("____________________________\nYour Character is the Air Wizard \n____________________________")
            user = AirWizard
            userstr = "Air Wizard"
        elif intselect%2 == 1:
            print("____________________________\nYour Character is the Water Wizard \n____________________________")
            user = WaterWizard
            userstr = "Water Wizard"
        elif intselect == 0:
            print("____________________________\nYour Character is the Fire Wizard \n____________________________")
            user = FireWizard
            userstr = "Fire Wizard"
    elif character == 2:
        intselect = int(random.random()*10)
        userClass = "Fighter"
        if intselect%2 == 0:
            print("____________________________\nYour Character is the Breserker \n____________________________")
            user = BreserkerFighter
            userstr = "Breserker Fighter"
        elif intselect%2 == 1:
            print("____________________________\nYour Character is the Rouge \n____________________________")
            user = RougeFighter
            userstr = "Rouge Fighter"
        elif intselect == 0:
            print("____________________________\nYour Character is the Monk \n____________________________")
            user = MonkFighter
            userstr = "Monk Fighter"
    else:
        character = int(input("Please enter 1 or 2 to pick your fighter \n 1: Ranged \n 2: Close Combat \n"))

def fight(x):
    i=0
    global opponentstr
    global outcome
    outcome = ""
    if x == 1 or x == 7: 
        opponent = AirWizard
        opponentstr = "Evil Air Wizard"
    elif x == 2 or x == 8: 
        opponent = BreserkerFighter
        opponentstr = "Evil Breserker Fighter"
    elif x == 3 or x == 9:
        opponent = WaterWizard
        opponentstr = "Evil Water Wizard"
    elif x == 4 or x == 10: 
        opponent = RougeFighter
        opponentstr = "Evil Rouge Fighter"
    elif x == 5:
        opponent = MonkFighter
        opponentstr = "Evil Monk Fighter" 
    elif x == 6:      
        opponent = FireWizard
        opponentstr = "Evil Fire Wizard"
    print("  ________________________________________________")
    print(" | You encountered a roaming Evil %s      |"%(opponentstr))
    print(" |________________________________________________|")
    while(user.hp > 0):
        outcome = "fighting"
        i+=1    
        if i%2 == 1:
            move = int(input("What do you want to do? \n1: Attack \n2: Check Stats \n3: Evade\n"))
            if move == 1:
                print("____________________________\nYou Attacked for %s damage" %(user.dmg))
                if opponent.armor > 0: 
                    opponent.armor = opponent.armor - user.dmg
                    if opponent.armor <= 0:
                        print("%s has 0 armor and %s hp left\n____________________________"% (opponentstr,opponent.hp))
                    else:
                        print("%s has %s armor and %s hp left\n____________________________"% (opponentstr,opponent.armor,opponent.hp))
                if opponent.armor <= 0:
                    opponent.hp = opponent.hp - user.dmg
                    print("%s has 0 armor and %s hp left\n____________________________" % (opponentstr,opponent.hp))
                    if opponent.hp <= 0: 
                        outcome == "win"
                        break
                if opponent.hp <= 0: 
                    outcome == "win"
                    break
            if move == 2:
                print("The evil %s stats are \nAttack: %s \nHitpoints: %s \nArmor: %s \nItem: %s" %(opponentstr,opponent.dmg,opponent.hp,opponent.armor,opponent.item))
            if move == 3:
                runchance = int(random.random()*10)
                if runchance%2 == 0 or runchance == 0:
                    outcome == "coward"
                    break
                else:
                    print("You failed to run away, the %s persues you" % (opponentstr))
        if i%2 == 0:
            print("____________________________\nYou were attacked by %s\nYour Took %s Damage!\n____________________________" % (opponentstr,opponent.dmg))
            if user.armor > 0: 
                user.armor = user.armor - opponent.dmg
                if opponent.armor <= 0:
                    print("____________________________\nYou have 0 armor and %s hp left\n____________________________"% (user.hp))
                else:
                    print("____________________________\nYou have %s armor and %s hp left\n____________________________"% (user.armor,user.hp))
            if user.armor <= 0:
                user.hp = user.hp - opponent.dmg
                if user.hp > 0:
                    print("____________________________\nYou have 0 armor and %s hp left\n____________________________"% (user.hp))
                if user.hp <= 0:
                    print("____________________________\nYou have 0 armor and 0 hp left\n____________________________")
                    outcome = "death"
                    break
        

def game():
    print("  ____________________________________________________________________________________________________________________________________________________")
    print(" | You wake up in a mysterious dungeon, with no memory of how you got here. You can't seem to find the exit, only hallways that lead to more hallways |")
    print(" |____________________________________________________________________________________________________________________________________________________|")
    print("  _________________________________")
    print(" | You try to remember who you are |")
    print(" |_________________________________|")
    charSelect()
    while True:    
        activity = int(input("What do you want to do? \n1: Search the dungeon for loot \n2: Hunt for beasts \n3: Check Stats \n4: Heal up\n5: Exit the game\n"))
        if activity == 1:
            itemchance = int(random.random()*100)
            if itemchance >= 10 and itemchance <= 20:
                print("____________________________\nYou found the legendary「Frying Pan」! \nDon't go alone, Take this! \nBonus damage for Fighters, useless for Wizards\n____________________________")
                if userClass == "Fighter":
                    user.dmg = user.dmg+20
                    user.item = "「Frying Pan」" 
            if itemchance >=0 and itemchance <= 10:
                print("____________________________\nYou found the mythical「Elder Wand」! \nYou feel its poweful aura \nBonus damage for Wizards, useless for fighters\n____________________________")
                if userClass == "Wizard":
                    user.dmg = user.dmg+20 
                    user.item = "「Elder Wand」" 
            else:
                print("You found nothing :(\n")
        if activity == 2:
            oppselect = int(random.random()*10)
            fight(oppselect)
            if outcome == "death":
                print("YOU DIED")
                break
            if outcome =="win":
                print("You defeat the %s and continue on your journey" % (opponentstr))
            if outcome =="coward":
                print("You ran away like the coward you are")    
        if activity == 3:
            print("Class: %s \nType: %s \nAttack: %s \nHitpoints: %s \nArmor: %s \nItem: %s " % (userClass,userstr,user.dmg,user.hp,user.armor,user.item))
        if activity ==4: 
            if user.hp <= 100:
                user.hp += 20
            if user.hp >= 100: 
                print("You are already healthy")
        if activity == 5:
            print("You give up your endless search for the exit, slowly growing insane, turning into an Evil %s. If you can't get out, no one can..."%(userstr))
            winsound.PlaySound("Death.mp3",winsound.SND_ASYNC)
            break
        if outcome == "death":
            print("YOU DIED")
            break
        if outcome =="win":
                print("You defeat the %s and continue on your journey" % (opponentstr))
        if outcome =="coward":
            print("You ran away like the coward you are")  
        if activity != 1 or activity != 2 or activity != 3 or activity != 4 or outcome =="fighting":
            print("\nPlease enter 1, 2 or 3 to perform an activity\n")
game()