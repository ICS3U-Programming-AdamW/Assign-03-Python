#!/usr/bin/env python3

# Created by: Adam Winogron
# Created on: April 28, 2022
# This program gets dimensions of a package from the user
# and tells them whether the shipping company will accept it

# include math
import math


# main function
def main():

    # Describe program function
    print("Welcome to Adam's shipping inc.")
    print("We only accept packages that are within our size and weight \
restrictions")

    # declare variables
    length_string = ""
    width_string = ""
    height_string = ""
    weight_string = ""

    # catch statement
    try:
        # ask the user for length of package
        length_string = input("The first thing I need is the \
length of your package in cm: ")
        length = float(length_string)
        print()

    except Exception:
        # tell the user their input wasn't an interger
        print()
        print("It seems that '{}' won't work for the length! \
I need a number to do math!".format(length_string))

        # conclusion scencance
        print()
        print("Bring us another package anytime!")

    else:
        try:
            # ask the user for the width of the package
            width_string = input("Next I'll need the width \
of the package in cm: ")
            width = float(width_string)
            print("")

        except Exception:
            # tell the user their input wasn't an interger
            print()
            print("It seems that '{}' won't work for the width! \
I need a number to do math!".format(width_string))

            # conclusion scencance
            print()
            print("Bring us another package anytime!")

        else:
            try:
                # ask the user for the height
                height_string = input("The next thing I need is the \
height of your package in cm: ")
                height = float(height_string)
                print()

            except Exception:
                # tell the user their input wasn't an interger
                print()
                print("It seems that '{}' won't work for the height! \
I need a number to do math!".format(height_string))

                # conclusion scencance
                print()
                print("Bring us another package anytime!")

            else:
                try:
                    # ask the user for the weight
                    weight_string = input("The last thing I need is the \
weight of your package in kilograms: ")
                    weight = float(weight_string)
                    print()

            # MATH
                    # calculate volume
                    base = length * width
                    volume = base * height

                    # compare values
                    if volume <= 9999 and weight <= 26:
                        print("Yup that works! We'll have the shipping \
information sent to you by email by 12pm tonight!")
                    else:
                        print("Sorry, that's gonna be too big for us to accept! \
Try Ferdaws shipping just down the road, they do oversized shipping!")

                except Exception:
                    # tell the user their input wasn't an interger
                    print()
                    print("It seems that '{}' won't work for the weight! \
I need a number to do math!".format(weight_string))

                finally:
                    # conclusion scencance
                    print()
                    print("Bring us another package anytime!")


# call main()
if __name__ == "__main__":
    main()
