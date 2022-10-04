#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: September 2022
# This program shows assignment statements


def main():
    # Defining Variables
    number_of_students = 2
    width = 11.5
    length = 5.5
    some_words1 = "Hello"
    some_words2 = "World!"

    # Using Assignment Statements
    number_of_students = number_of_students + 5
    area_of_rectangle = length * width
    hello_world = some_words1 + ", " + some_words2

    # Outputs the number of students, area of a rectangle and "Hello, World!" to console.
    print("The number of students is: " + str(number_of_students))
    print("The area of a rectangle is: " + str(area_of_rectangle) + " cm²")
    print(hello_world)

    print("\nDone.")


if __name__ == "__main__":
    main()
