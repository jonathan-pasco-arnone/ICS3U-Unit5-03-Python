#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program determines you grade middle percentage


def which_mark(mark):
    # This function determines you grade middle percentage

    if mark == "4+":
        mark_percent = 97
        return mark_percent
    elif mark == "4":
        mark_percent = 90
        return mark_percent
    elif mark == "4-":
        mark_percent = 83
        return mark_percent
    elif mark == "3+":
        mark_percent = 78
        return mark_percent
    elif mark == "3":
        mark_percent = 75
        return mark_percent
    elif mark == "3-":
        mark_percent = 71
        return mark_percent
    elif mark == "2+":
        mark_percent = 68
        return mark_percent
    elif mark == "2":
        mark_percent = 64
        return mark_percent
    elif mark == "2-":
        mark_percent = 61
        return mark_percent
    elif mark == "1+":
        mark_percent = 58
        return mark_percent
    elif mark == "1":
        mark_percent = 54
        return mark_percent
    elif mark == "1-":
        mark_percent = 51
        return mark_percent
    elif mark == "R":
        mark_percent = 24
        return mark_percent
    else:
        return "-1"


def main():

    mark = str(input("Please enter a mark: "))
    print("")

    mark_percent = which_mark(mark)

    if mark_percent == "-1":
        print("-1")
    elif mark_percent == 24:
        print("You have a middle percentage mark of"
              " {0}% (You failed this class)".format(mark_percent))
    else:
        print("You have a middle percentage mark of {0}%".format(mark_percent))


if __name__ == "__main__":
    main()
