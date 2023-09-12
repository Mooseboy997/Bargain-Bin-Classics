"""
BARGAIN_BIN_CLASSICS_DRAGONS_DEN

Description:
"""
import random
print("NPC: \"I have a quest for you, there is a dragon in the town.  You must defeat it.\"")
answer = input("would you like to accept, or decline?")
if answer == "decline":
    print("OK YOUR ADVENTURE IS OVER BECAUSE YOU CHOSE TO BE A NERD!")
if answer == "accept":
    print("NPC: \"Ok, cool. he is in a cave across town from here,here is a map, and good luck\"")
    print("you start heading, across town, and you get approached by a stranger")
    answer_2 = input("NPC: \"I have brought you a potion of strength, would you like to drink it?\"yes or no")
    if answer_2 == "yes":
        print("You die from poisoning")
    elif answer_2 == "no":
        print("Good choice, that potion was poisoned")
        print("You keep walking down the road, and you a aproached by someone trying to give away a sword")
        answer_3 = input("NPC: \"I have a sword for you, would you like it?\"yes or no")
        if answer_3 == "no":
            print("You go around collecting rocks to throw at it.")
            encounter = input("You encounter a team of bandits, do you fight, or run?")
            if encounter == "fight":
                encounter_part_two = input("You start throwing rocks, at them, but they pull out their, daggers, do you run, or continue?")
                if encounter_part_two == "continue":
                    print("You try to fight them off, but they all stab you.")
                if encounter_part_two == "run":
                    print("You run away, and they just stand there.")
                    print("You run through the woods, and, you find a camp")
                    decision = input("Do you stay, or leave?")
                    if decision == "stay":
                        print("You stay, at that , camp, but it's owners come, back, and it turns out it was a bandit camp, and they all stab you.")
                    if decision == "leave":
                        print("You leave the camp, and find your way back to town")
                        town_2 = input("Would you like to explore, or leave?")
            if encounter == "run":
                print("You re-enter town,")
                town = input("you find a cozy inn to stay the night.  Do you stay, or do you leave?")
                if town == "stay":
                    print("You fall asleep, and a bandit stabs you in the eye.")
                if town == "leave":
                    print("An elderly lady walks up to you")
                    quest = input("NPC: \"My cat is missing, and I cannot find him anywhere.\"do you look, or do you leave")
                    if quest == "look":
                        print("NPC: \"Thankyou so much\"")
                        where = input("Would you like to look, forest, or around town")
                        if where == "around town":
                            print("he is nowhere to be found.")
                            print("you are spotted, and killed by bandits.")
                        if where == "forest":
                            print("you find him in a cave.  But there is a sleeping dragon in there.")
                            where_2 = input("do you get him, or get help?")
                            if where_2 == "get him":
                                print("you try to get him, but you wake the sleeping dragon.")
                                second_encounter = input("do you fight, or come back later?")
                                if second_encounter == "fight":
                                    print("You don't have any weapons, so you die")
                                if second_encounter == "come back later":
                                    print("You head back into town, and tell the lady about the dragon, and she creates a mob at the town square.")
                                    print("You have now taken control of mob")
                                    cowardice_ending = input("You make your way to the cave and see the dragon, do you send your bandits, or the whole mob?")
                                    if cowardice_ending == "whole mob":
                                        print("The entire mob runs in, and the dragon burns them all.")
                                    if cowardice_ending == "bandits":
                                        print("The bandits run in and stab the dragon to death.  But the dragon's baby comes in, and the bandits scatter, and start shooting it with a bow and arrow, and it dies, then the town, gets the treasure, and keeps, it , and no-one is taxed for the next 3 years.  Congratulations, you have unlocked the cowardice ending!")
                    if quest == "leave":
                        print("You tell the Npc that you don't have the time")
                        no_cat = input("Would you like to continue, to the dragon's den, or explore town?")
                        if no_cat == "explore town":
                            print("You go exploring town, and you encounter an old man, selling guns, and the bible.")
                            purchase = input("do you buy guns, bible, or nothing, you cannot get them both")
                            if purchase == "guns":
                                print("NPC: \"good choice, you can kill the dragon, in one shot.\" You have added gun to your inventory, along with one single bullet:)")
                                print("You head back on the path, and you find a goblin.  You try to shoot it.")
                                shot = random.randint(1, 2)
                                if shot == 1:
                                    print("You miss the shot, and the goblin stabs you in the eye.")
                                if shot == 2:
                                    print("You have succeeded, and you took another bullet from his pocket, but in the distance you hear a noise, like a bunch of other goblins running, towards you.")
                                    choice = input("do you run, or do you stay")
                                    if choice == "stay":
                                        print("The other golbins, get there, and proceed to stab you")
                                    if choice == "run":
                                        print("You run around the forest a while, and get hungry, you see some berries and you eat them.")
                                        food = random.randint(1, 3)
                                        if food == 1:
                                            print("you eat them, and you are no longer hungry.")
                                            print("You enter the dragons den, and you see it, and it lets out a roar.")
                                            boss_fight = input("Do you shoot it or do you throw rocks at it?")
                                            if boss_fight == "throw rocks at it":
                                                print("You die, because they are rocks, going against an adult dragon.")
                                            if boss_fight == "shoot it":
                                                final_shot = random.randint(1, 2)
                                                if final_shot == 1:
                                                    print("you shoot the dragon, and it hits him right in the eye and he dies.")
                                                    baby = random.randint(1, 2)
                                                    if baby == 1:
                                                        print("But the baby dragon comes in for revenge.  You try to throw a rock at it and you miss, and the baby dragon eats you")
                                                    if baby == 2:
                                                        print("But the baby dragon comes in for revenge.  You try to throw a rock at it, and it hits the baby in the eye.  Congratulations, you have won the randomized, ending!")
                                                if final_shot == 2:
                                                    print("You miss, and the dragon, eats you.")
                                        if food == 2:
                                            print("Those berries were poisonous, so you die")
                                        if food == 3:
                                            print("A goblin runs in, and stabs you in the eye.")
                            if purchase == "bible":
                                print("NPC:  \"Good, choice, maybe the power of god can help you kill the dragon.\" You have added bible to your inventory")
                                print("You, go down the path, and encounter a demon.")
                                guess = input("The demon, is thinking of a number, if you guess lower, you live.")
                                if guess < 38:
                                    print("You have passed the test, and may go on.")
                                if guess > 38:
                                    print("A pit opens up, and you fall down to hell, oh yeah, by the way, you were going to hell anyway.  Congratulations you have unlocked, the counterfeit bible ending.")
                            if purchase == "none":
                                print("The old man, shoots you with th gun.")
                                gun = random.randint(1, 2)
                                if gun == 1:
                                    print("You dodge the shot, and as reward, the man gives you the gun with 10 bullets, but a bandit finds you, and stabs you in the eye before you can do anything.")
                                if gun == 2:
                                    print("You get shot in the head, and die.")
        if answer_3 == "yes":
            print("You now have a sword in your inventory.  You then start collecting rocks to throw at it, just in case.")
            print("you continue walking down the path, and you are approached by a stranger")
            answer_4 = input("NPC: \"I heard, that you are going to be fighting the dragon, across town.  Here, take this loaf of bread so that you don't get hungry\"yes or no")
            if answer_4 == "no":
                print("you die of hunger")
            if answer_4 == "yes":
                print("you are no longer hungry")
                print("You head to a stream and take a drink")
                drink = random.randint(1, 2)
                if drink == 1:
                    print("you die, because the water is unclean")
                if drink == 2:
                    print("you are no longer thirsty")
                    print("you are now aproaching the den of the dragon")
                    print("you are in the den, and you see the massive dragon, which is white, and has massive wings.  It opens a mouth, and lets out a bellowing roar")
                    slay = input("what weapon do you choose, rocks or sword.")
                    if slay == "sword":
                        print("YOU HAVE SLAIN THE MIGHTY DRAGON!  But, as you exit the den, you trip on a rock, that you have placed down for no reason, and fall off of a cliff.  But you don't die yet, the baby dragon, comes for revenge, and eats you.  Congratulations, you have earned, the heroic death, ending!")
                    if slay == "rocks":
                        print("You throw a rock at it, and it does nothing.  It shoots its fire breath at you, and you die.")
    
    

        
