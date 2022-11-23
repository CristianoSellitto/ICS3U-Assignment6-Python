#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in November 2022
# A program that calculates a sphere's area and volume

import math


def main():
    # Calculates a sphere's area and volume

    print("\nThis program calculates a sphere's surface area and volume")
    print("A = 4πr²")
    print("V = (4 ÷ 3) × πr³")
    try:
        radius_text = input("\nEnter the sphere's radius: ")
        radius_number = float(radius_text)
        surface_area = 4 * math.pi * radius_number**2
        volume = (4 / 3) * math.pi * radius_number**3
        print("\nThis sphere's surface area is {}cm²".format(surface_area))
        print("This sphere's volume is {}cm³".format(volume))
    except ValueError:
        print("\nYou did not input a number. (ValueError)")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
