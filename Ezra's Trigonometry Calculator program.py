# Make a program that can calculate the length of sides
# of a triangle and the interior angels of a triangle (right angled)
# CONVERT FROM RADIANS TO DEGREES
# Radians to degrees formula: radians * (180/pi) or use math.degrees(x)
# math.pow (x, y) for powers, x is value, y is power
# math.pi = pi
# 3, 4, 5 for triangle sides for testing
import math
import sys


def intcheck(x):  # Procedure for checking for integers
    try:  # Attempt to convert to integer
        x = int(x)
    except:  # if not an integer
        x = ''

    # To ensure number entered is more than zero
    while x == '':  # Loop for input
        x = input("\nPlease enter a number ")
        try:  # Attempt integer check again
            x = int(x)
        except:
            x = ''
            print ("Not a number")
    return (x)  # Return integer value

def positive_check (x):
    if x == 0:
        print ("The number you entered was zero,"
               " which is impossible to calculate with")
        x = ''
        return x
    elif x < 0:
        print ("The number you entered was a negative,"
               " which is impossible to calculate with")
        x = ''
        return x
    else:
        return x

def sohcahtoa(a, b, c, d):  # Procedure for SOHCAHTOA formula
    # a = known side, b = known side value, c = unknown side, d = angle
    b = float(b)  # convert to float
    d = float(d)

    if a.lower() == 'a':
        if c.lower() == 'o':
            return ((math.tan(math.radians(d))) * b)
        elif c.lower() == 'h':
            return (b / (math.cos(math.radians(d))))

    elif a.lower() == 'o':
        if c.lower() == 'a':
            return (b / (math.tan(math.radians(d))))
        elif c.lower() == 'h':
            return (b / (math.tan(math.radians(d))))

    elif a.lower() == 'h':
        if c.lower() == 'a':
            return ((math.cos(math.radians(d))) * b)
        elif c.lower() == 'o':
            return ((math.sin(math.radians(d))) * b)


def inverse(a, b, c, d):  # Inverse SOHCAHTOA calculations
    # a = known side, b = known side value,
    # c = other known side, d = other known side value
    b = float(b)
    d = float(d)

    if a.lower() == 'o':
        if c.lower() == 'h':
            return (math.degrees(math.asin(b / d)))
        elif c.lower() == 'a':
            return (math.degrees(math.atan(b / d)))

    elif a.lower() == 'h':
        if c.lower() == 'a':
            return (math.degrees(math.acos(d / b)))
        elif c.lower() == 'o':
            return (math.degrees(math.asin(d / b)))

    elif a.lower() == 'a':
        if c.lower() == 'o':
            return (math.degrees(math.atan(d / b)))
        elif c.lower() == 'h':
            return (math.degrees(math.acos(b / d)))


def main():  # Procedure for main program allowing it to be looped
    global exit, f
    exit = ''
    angle = 0
    answer = 0
    count = 0
    hypotenuse = ''
    option = ''
    option2 = ''
    side = ''
    side2 = ''
    unknown_side = ''

    while option.lower() not in ['yes', 'y', 'no', 'n']:  # Error checking
        # Are 2 sides provided?
        option = input("\nAre the lengths of 2 sides provided? ")
        if option.lower() not in ['yes', 'y', 'no', 'n']:
            print ("Please enter a proper response")

    if option.lower() in ['yes', 'y']:  # If user has lengths of 2 sides
        f.write('Lengths of 2 sides known')
        while option2.lower() not in ['yes', 'y', 'no', 'n']:
            # Is third side needed?
            option2 = input("\nDo you need to find a third side? ")
            if option2.lower() not in ['yes', 'y', 'no', 'n']:
                print ("Please enter a proper response")

        # Finding side lengths path
        if option2.lower() in ['yes', 'y']:  # If user needs to find third side
            f.write('\nLength of third side needed')
            while hypotenuse.lower() not in ['yes', 'y', 'no', 'n']:
                # Ask if length of hypotenuse is given
                hypotenuse = input("\nDo you know the length of"
                                   " the hypotenuse side? ")
                if hypotenuse.lower() not in ['yes', 'y', 'no', 'n']:
                    print ("Please enter a proper response")
            # If length of hypotenuse is given
            if hypotenuse.lower() in ['yes', 'y']:
                # Ask for length
                hypotenuse = input("\nLength of hypotenuse side? ")
                hypotenuse = intcheck(hypotenuse)
                hypotenuse = positive_check(hypotenuse)
                while hypotenuse == '':
                    hypotenuse = input("\nLength of hypotenuse side? ")
                    hypotenuse = intcheck(hypotenuse)
                    hypotenuse = positive_check(hypotenuse)                    

                adjacent = input("\nLength of other side? ")  # Ask for length
                adjacent = intcheck(adjacent)
                adjacent = positive_check(adjacent)
                while adjacent == '':
                    adjacent = input("\nLength of other side? ")
                    adjacent = intcheck(hypotenuse)
                    adjacent = positive_check(hypotenuse)                  

                # Ensure hypotenuse is longest side
                
                while adjacent >= hypotenuse:
                    print ("That isn't mathmetically correct, the hypotenuse"
                           " is the longest length")
                    adjacent = input("\nLength of other side? ")
                    adjacent = intcheck(adjacent)
                    adjacent = positive_check(adjacent)
                    while adjacent == '':
                        adjacent = input("\nLength of other side? ")
                        adjacent = intcheck(hypotenuse)
                        adjacent = positive_check(hypotenuse)                    

                hypotenuse = float(hypotenuse)
                adjacent = float(adjacent)
                f.write('\nThe length of the hypotenuse is ')
                f.write(str(hypotenuse))
                f.write('\nThe length of the other side is ')
                f.write(str(adjacent))

                try:
                    # Calculate missing side, if negative
                    # value cannot be square rooted
                    missing = math.sqrt((math.pow(hypotenuse,
                                         2) - (math.pow(adjacent, 2))))
                except:
                    print ("\nIt appears the calculation could not be done"
                           "because a negative value cannot be square rooted")
                    print ("Are you sure you've put in the correct values?")
                    main()
                print ('The length of your unknown side is', missing)  # Answer
                f.write('\nThe length of the unknown side is ')
                f.write(str(missing))
                f.write('\n')

            # If length of hypotenuse is not given
            elif hypotenuse.lower() in ['no', 'n']:
                # Ask for length
                opposite = input("\nLength of the first side? ")
                opposite = intcheck(opposite)
                opposite = positive_check(opposite)
                while opposite == '':
                    opposite = input("\nLength of first side? ")
                    opposite = intcheck(opposite)
                    opposite = positive_check(opposite)                    

                # Ask for length
                adjacent = input("\nLength of other side? ")  # Ask for length
                adjacent = intcheck(adjacent)
                adjacent = positive_check(adjacent)
                while adjacent == '':
                    adjacent = input("\nLength of the other side? ")
                    adjacent = intcheck(hypotenuse)
                    adjacent = positive_check(hypotenuse)

                opposite = float(opposite)
                adjacent = float(adjacent)
                f.write('\nThe length of your 2 known sides is ')
                f.write(str(opposite))
                f.write(' and ')
                f.write(str(adjacent))

                # Calculations
                missing = math.sqrt((math.pow(opposite,
                                    2) + (math.pow(adjacent, 2))))
                print ('The length of the hypotenuse is', missing)  # Answer
                f.write('\nThe length of the hypotenuse is ')
                f.write(str(missing))
                f.write('\n')

        # If finding angle
        elif option2.lower() in ['no', 'n']:
            print ('\nYou should have the length of two sides,'
                   ' and are trying to find the angle')
            print ("A is the adjacent side to the angle,")
            print ("O is the side opposite of the angle,")
            print ("and H is the hypotenuse")

            # Check only recognized inputs
            while side.lower() not in ['a', 'o', 'h']:
                side = input('\nOut of A, O, and H, which side is provided? ')
                if side.lower() not in ['a', 'o', 'h']:
                    print ("That's not one of the options")

            side_value = input("What is the value of this side? ")
            side_value = intcheck(side_value)
            side_value = positive_check(side_value)
            while side_value == '':
                side_value = input("\nWhat is the value of this side? ")
                side_value = intcheck(side_value)
                side_value = positive_check(side_value)

            # Check only recognized inputs that haven't been picked
            while side2.lower() not in ['a', 'o',
                                        'h'] or side2.lower() == side.lower():
                side2 = input("\nWhich other side is provided?"
                              " (out of A, O, and H) ")
                if side2.lower() not in ['a', 'o',
                                         'h'] or side2.lower() == side.lower():
                    print ("That's not one of the options, "
                           "or you've chosen that option before")

            side2_value = input("What is the value of this side? ")
            side2_value = intcheck(side2_value)
            side2_value = positive_check(side2_value)
            while side2_value == '':
                side2_value = input("\nWhat is the value of this side? ")
                side2_value = intcheck(side2_value)
                side2_value = positive_check(side2_value)
            # If user enters value ihgher than hypotenuse
            if side.lower() == 'h':
                while side2_value >= side_value:
                    print ("That isn't mathmetically correct, "
                           "the hypotenuse is the longest length")
                    side2_value = input("\nWhat is the value of this side? ")
                    side2_value = intcheck(side2_value)
                    side2_value = positive_check(side2_value)
                    while side2_value == '':
                        side2_value = input("\nWhat is the value of this side? ")
                        side2_value = intcheck(side2_value)
                        side2_value = positive_check(side2_value)
            elif side2.lower() == 'h':
                while side2_value <= side_value:
                    print ("That isn't mathmetically correct, "
                           "the hypotenuse is the longest length")
                    side2_value = input("\nWhat is the value of this side? ")
                    side2_value = intcheck(side2_value)
                    side2_value = positive_check(side2_value)
                    while side2_value == '':
                        side2_value = input("\nWhat is the value of this side? ")
                        side2_value = intcheck(side2_value)
                        side2_value = positive_check(side2_value)                    

            side_value = float(side_value)
            side2_value = float(side2_value)
            f.write('\nThe length of side ')
            f.write(side.upper())
            f.write(' is ')
            f.write(str(side_value))
            f.write('\nThe length of side ')
            f.write(side2.upper())
            f.write(' is ')
            f.write(str(side2_value))

            answer = inverse(side, side_value, side2, side2_value)
            print ('Your answer is', answer)
            f.write('\nThe size of the angle is ')
            f.write(str(answer))
            f.write('\n')

    # If user needs to find a missing length with angle
    elif option.lower() in ['no', 'n']:
        f.write('\nOne side length and an angle is known')
        print ('\nYou should have the length of one side, '
               'and one angle provided')
        print ('and are trying to find the length of a side')
        print ("A is the adjacent side to the angle,")
        print ("O is the side opposite of the angle,")
        print ("and H is the hypotenuse")

        while side.lower() not in ['a', 'o', 'h']:
            side = input("\nOut of A, O, and H, which side is provided? ")
            if side.lower() not in ['a', 'o', 'h']:
                print ("That's not one of the options")

        side_value = input("\nWhat is the value of this side? ")
        side_value = intcheck(side_value)
        side_value = positive_check(side_value)
        while side_value == '':
            side_value = input("\nWhat is the value of this side? ")
            side_value = intcheck(side_value)
            side_value = positive_check(side_value)
        
        angle = input("\nWhat is the value of the angle "
                      "provided (in degrees)? ")
        angle = intcheck(angle)
        angle = positive_check(angle)
        while angle == '':
            angle = input("\nWhat is the value of the angle "
                          "provided (in degrees)? ")
            angle = intcheck(angle)
            angle = positive_check(angle)
        #If user enters angle bigger than 90 degrees
        while angle >= 90:
            print ('Sorry, but in a right-angled triangle, '
                   'there cannot be an angle bigger than 90 degrees')
            angle = input("\nWhat is the value of the angle "
                          "provided (in degrees)? ")
            angle = intcheck(angle)
            angle = positive_check(angle)
            while angle == '':
                angle = input("\nWhat is the value of the angle "
                              "provided (in degrees)? ")
                angle = intcheck(angle)
                angle = positive_check(angle)            

        # Check only recognized inputs that haven't been picked
        while unknown_side.lower() not in ['a', 'o',
                                           'h'] or unknown_side.lower() == side.lower():
            unknown_side = input("\nOut of A, O and H, which side"
                                 " do you need to find the length of? ")
            if unknown_side.lower() not in ['a', 'o',
                                            'h'] or unknown_side.lower() == side.lower():
                print ("That's not one of the options, or"
                       " you've chosen that option before")

        side_value = float(side_value)
        angle = float(angle)

        f.write('\nThe length of the known side ')
        f.write(side.upper())
        f.write(' is ')
        f.write(str(side_value))
        f.write('\nThe size of the angle is ')
        f.write(str(angle))
        f.write('\nThe length of the side ')
        f.write(unknown_side.upper())
        f.write(' is unknown')

        answer = sohcahtoa(side, side_value, unknown_side, angle)
        print ('The length of the side', unknown_side.upper(), 'is', answer)
        f.write('\nThe length of the side ')
        f.write(unknown_side.upper())
        f.write(' is ')
        f.write(str(answer))
        f.write('\n')

    print ("\nHopefully this program has helped"
           " you in one of your math problems")
    while exit.lower() not in ['y', 'yes', 'n', 'no']:  # Exit system or not
        exit = input('\nWould you like to continue using this program? ')
        if exit.lower() not in ['y', 'yes', 'n', 'no']:
            print ("That's not one of the options")
    if exit.lower() in ['y', 'yes']:
        print ("____________________________________________")
        main()
    elif exit.lower() in ['n', 'no']:
        print ("---------------------------------")
        print ("Thank you for using this program!")
        print ("---------------------------------")
        print ("Here is your history list of all your calculations")
        f.close()
        f = open('History.txt', 'r')
        print (f.read())
        # To stop screen from collapsing on exit
        holder = input('Press enter to exit')
        sys.exit()  # Exit

print ("____________________________________________________")
print (" __      __        __")
print ("/  \    /  \ ____ |  |   ____  ____   _____   ____  ")
print ("\   \/\/   // __ \|  | _/ __ \/ __ \ /     \_/ __ \ ")
print (" \        /\  ___/|  |_\  \__( |__| )  Y Y  \  ___/ ")
print ("  \__/\__/  \____ |____/\____ \____/|__|_|__/\____  ")
print ("____________________________________________________\n")
print('This tool is designed to help you calculate the '
      '\nvarious sides and angles of a right-angled triangle.')
print ("Please note that if your problem/question "
       "cannot be solved via trigonometry if: ")
print ("- The triangle is not right-angled, and the height is not provided")
print ("- You are only provided the angle value, "
       "or only the length of one side")
print ("\nNOTE: Remember that a non right-angled triangle "
       "can be split into 2 right triangles!")
print ('\n*Remember to convert all measurements of the '
       'triangle into the same unit!*')
print ("____________________________________"
       "________________________________________")

while True:
    exit = ''
    f = open('History.txt', 'w')
    main()
