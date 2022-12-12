#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in November 2022
# A program that calculates a sphere's volume

import math


def volume_of_a_sphere(radius):
    # Calculates a sphere's volume

    volume = (4 / 3) * math.pi * radius**3

    return volume


def main():
    # Gets input and calls the function above

    print("\nThis program calculates a sphere's volume.")
    print("V = (4 ÷ 3) × πr³")
    try:
        radius_text = input("\nEnter the sphere's radius: ")
        radius_number = float(radius_text)
        volume_number = volume_of_a_sphere(radius_number)
        print("\nThis sphere's volume is {}cm³".format(volume_number))
    except ValueError:
        print("\nYou did not input a number. (ValueError)")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
