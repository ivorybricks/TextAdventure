import time

# intro message
start = '''
You wake up in a pitch black room.
Your head is throbbing, and you can't place
who you are, or where you are.
You become aware of the cold air enveloping you,
sending shivers up your spine.
'''

# prompt for incorrect user inputs
    def tryAgain() :
    print('Incorrect input. Try again.')
    time.sleep(3)


print(start)

done = False

while done != True:

    
    time.sleep(3)
    print('\nYou have a choice. Will you wait for something to happen, or will you move around to see if you can find something?\n(wait OR move)')
    user_input = input()

    if user_input == 'wait' :
        print('\nYou wait, realizing that you are sitting on the floor.\nSuddenly, the lights flicker on, revealing a small, dingy room \nand a door in front of you.\nIt says PROPERTY OF WILLIAMSBURG INSANE ASYLUM.')
        time.sleep(3)
        print('\nWill you look around your room or escape out the door?\n(look around OR escape)')
        user_input = input()

        if user_input == 'look around' :
            print('\nYou explore the cramped room. You find a picture of two people on the desk to your right.\nThere is a wardrobe by the desk. You open it and see a couple changes of clothes.\nAfter closing the wardrobe, you turn around and see a bed.\nThere is a tattered journal on the bed.')
            time.sleep(3)
            print('\nDo you look through the journal, or escape out the door?\n(look OR escape)')
            user_input = input()

            if user_input == 'look' :
                print('\nYou take the journal and open it, but the handwriting is unintelligible.\nBefore you can flip through the pages, a man bursts in through the door\nand throws something at you. Your vision fades as you gasp in pain.')
                time.sleep(3)
                print('\nYou are dead.')

                done = True

            elif user_input == 'escape':
                print('\nYou open the heavy door to go out\nand find yourself in a swarm of people running across the halls.\nIn the midst of the crowd, you spot a broken window.')
                time.sleep(3)
                print('\nDo you walk or run toward the window to get out?\n(walk OR run)')
                user_input = input()

                if user_input == 'walk':
                    print('\nYou begin to head toward the window.\nOn the way out, you see a man in a wheelchair out of the corner of your eye.')
                    time.sleep(3)
                    print('\nHe nods at you as you continue to the window.\nYou climb out to your freedom.')
                    done = True


                if user_input == 'run' :
                    print('\nYou run to the window until you are within arm\'s reach.\nHowever, a man sitting in a wheelchair to your right\ngets up and runs toward you.\nHe tackles and strangles you as you struggle to break free.')
                    time.sleep(3)
                    print('\nYou are dead.')

                    done = True

        elif user_input == 'escape':
            print('\nYou open the door and run out in a sluggish gait.\nYou see a broken window and realize that you can escape.')
            time.sleep(3)
            print('\nDo you run, or walk to escape?\n(run OR walk)')
            user_input = input()

            if user_input == 'walk':
                print('\nYou begin to head toward the window.\nOn the way, you see a man in a wheelchair out of the corner of your eye.\nHe nods at you as you continue to the window.\nYou climb out to freedom.')
                done = True

            if user_input == 'run':
                print('\nYou run to the window until you are within arm\'s reach.\nHowever, a man sitting in a wheelchair to your right\ngets up and runs toward you.\nHe tackles and strangles you as you struggle to break free.')
                time.sleep(3)
                print('\nYou are dead.')
                done = True

    elif user_input == 'move' :
        print('\nYou move around and feel your arm hit something hard and cold.\nYou run your hands along the object and realize that it is a bed.\nSuddenly, you hear footsteps nearing your door.')
        time.sleep(3)
        print('\nDo you hide under the bed, or sit still and surrender yourself?\n(hide OR surrender)')
        user_input = input()

        if user_input == 'surrender' :
            print('\nYou surrender.\nYou hear the door open and the lights turn on, revealing an unkempt man.\nHe rushes toward you and strikes you in the head\nbefore you can let out a scream.')
            time.sleep(3)
            print('\nYou are dead.')
            done = True

        elif user_input == 'hide':
            print('\nYou crawl underneath the bed and hold your breath.\nYou hear the door squeak open and hear the footsteps in the room.\nFrom beneath the bed, you see the lights turn on, revealing a pair of shoes which belong to a man.\nThe shoes shuffle around the room before they begin to head back out the door,\nwhich says PROPERTY OF WILLIAMSBURG INSANE ASYLUM.')
            time.sleep(3)
            print('\nDo you take off your shoe and climb out to throw it at him, or wait for him to walk out so you can peer out the door?\n(throw shoe OR peer out)')
            user_input = input()

            if user_input =='peer out':
                print('\nThe man exits, leaving the door open.\nYou get out from under the bed and walk to the door.\nWhen you peek out, you notice a crowd of people running back and forth across the halls.\nYou also see a man sitting in a wheelchair by a broken window.')
                time.sleep(3)
                print('\nThe man gets up and walks away.\nYou run toward the window and climb out to freedom.')
                done = True

            elif user_input == 'throw shoe':
                print('\nYou climb out from your hiding spot and chuck your shoe at the man.\nHe hunches down, appearing to be severely wounded.\nYou take a few steps toward him.\nBut, he recovers, turning around and kicking you.\nYour vision fades as he lands more blows.')
                time.sleep(3)
                print('\nYou are dead.')
                done = True

    else :
        tryAgain()
        done = False
