#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in November 2022
# A program that calculates a sphere's volume

import math


def volume_of_a_sphere():
    # Calculates a sphere's volume

    print("\nThis program calculates a sphere's volume.")
    print("V = (4 ÷ 3) × πr³")
    try:
        radius_text = input("\nEnter the sphere's radius: ")
        radius_number = float(radius_text)
        volume = (4 / 3) * math.pi * radius_number**3
        print("\nThis sphere's volume is {}cm³".format(volume))
    except ValueError:
        print("\nYou did not input a number. (ValueError)")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    volume_of_a_sphere()
