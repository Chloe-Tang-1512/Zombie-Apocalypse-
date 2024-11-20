name = input("What is your name? > ")
age = 11
is_smart = True
choice = "Snake"
custom_theme = "Aqua"

#my_variables/random stuff from my first CSCT lesson :)

print("Hello world")
print("Hello " + name)
print("You are in a zombie apocalypse.")
print("It is caused by the UD-virus.")
print("Try to save the city by finding useful items.")
print("Or even better, the cure.")
print("Always trust your instict and do the right thing.")
print("Good luck!")
print("------------------------------------------------------------")

print("You are outside three buildings: a hospital, police station and a military base.")
place = input("Which one do you want to enter? > ")

if place == "police station" or place == "Police Station" or place == "Police station":
    print("You have entered the police station.")
    print("There are three doors in front of you. OB, PB and IR.")
    door_p = input("Which one do you want to enter? > ")

    if door_p == "OB":
     print("This is the office block.")
     print("You walk striaght to the office labelled Sherriff's office.")
     eon = input("Do you enter? > ")

     if eon == "yes":
      print ("The sherriff turns round and points a gun at you.")
      life = input("Do you run away? > ")

      if life == "yes":
       print("As you run, the sheriff fires and hits you.")
       print("GAME OVER")

      if life == "no":
       print("The sherriff lowers the gun and tells you that he is not to be disturbed.")
       print("You turn and go back to the reception area.")

     if eon == "no":
      print("You enter a side office and find a grenade, which you take.")

    if door_p == "PB":
     print("This is the prison block.")
     print("You find a row of prison cells.")
     epn = input("Do you enter one of the prison cells? > ")

     if epn == "yes":
      print("You enter and a prisoner pounces at you.")
      dec = input("Do you run or fight? > ")

      if dec == "run":
       print("You run and lock the door behind you. You are back at the reception area.")

      if dec == "fight":
       print("You fight the prisoner and you overpower him.")
       print("You return to the reception area after locking the cell door.")

     if epn == "no":
      print("You turn back and return to the reception area.")

    if door_p == "IR":
     print("You are in the interrogation rooms.")
     print("There are voices coming from the room closest to you.")
     ein = input("Do you want to enter? > ")

     if ein == "no":
      print("You enter the room at the end instead and find a tazer, whi-ch you take.")
      print("You return to the reception area.")

     if ein == "yes":
      print("You enter, but immediately leave after you see that there is a busy officer.")


if place == "hospital" or place == "Hospital":
    print("You are now in the hospital in the reception area.")
    print("There are three doors in front of you: QB, HW and IC.")
    block = input("Which door do you want to enter? > ")

    if block == "QB":
        print("This is the Quarantine Block! Proceed with caution...")
        print("There are two doors, D and S.")
        safety = input("Which do you enter? > ")

        if safety == "D":
            print("You enter the room and find that it is filled with infected people.")
            print("Very soon you are also infected.")
            print("GAME OVER")

        if safety == "S":
            print("You find a room full of biohazard suits and the ingredients to the cure")
            print("You then return to the reception area.")

    if block == "HW":
        print("You are in the Hospital Wards.")
        print("A nurse hurries towards you, asking for help.")
        helper = input("Do you help her? > ")

        if helper == "yes":
             print("She asks you to hand over some batterries.")
             print("You do so and she thanks you.")
             print("You return to the reception as a hero.")
            
        if helper == "no":
            print("She frowns and infects you with the UD-virus.")
            print("GAME OVER")

    if block == "IC":
        print("You are in the Intensive Care Unit.")
        print("There are two corridoors: LS and RC.")
        corr = input("Which one do you want to enter? > ")

        if corr == "LS":
            print("This corridoor was the life support corridoor.")
            print("A stressed doctor shouts at you and calls security, who drags you out.")
            print("GAME OVER")

        if corr == "RC":
            print("You are in the recovery centre.")
            print("You find a metal ball, which you take.")
            print("You return to the reception area.")

if place == "military base"or place == "Military base"or place == "Military Base":
    print("You have entered the military base, where you encounter a...problem.")
    print("There is an electric fence topped with barbed wire.")
    wire = input("Do you cut (the wires) or call (for assistance)? > ")

    if wire == "cut":
        print("You use bolt cutters to snip the wires.")
        print("You pass through the fence unharmed.")
        print("However,an alarm goes off and armed guards rush towards you.")
        gun = input("Do you run or explain(your mission)? > ")

        if gun == "run":
            print("You run, but you shange your mind when the gun is pointing at you.")
            print("GAME OVER")

        if gun == "explain":
            print("The guards seem relieved and offer to help you on your mission.")
            print("With their help, you manage to find the source of the UD-Virus.")
            print("It is a nuclear power plant on a remote island nearby.")
            print("Part 2 coming soon!")
            print("For now, you have beaten the game! Well done!")

    if wire == "call":
        print("You call for help and armed soldiers march towards you.")
        print("They DO look rather intimidating.")
        print("Unfortunately, the decide that you are hostile and arrest you.")
        print("GAME OVER")

        

    
    
            
        
        
        
        

    
      

     
 
