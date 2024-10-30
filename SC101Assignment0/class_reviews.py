"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
END = '-1'

def main():
    """
    TODO:
    """
    oneone = 0
    oone = 0
    oneone_count = 0
    oneone_max = 0
    oneone_min = 101
    oone_max = 0
    oone_min = 101
    oone_count = 0
    while True:
        classes = input("Which class? ")
        if classes == END:
            if oone_count == oneone_count == 0:
                print("No class scores were entered", end="")
            elif oone_count == 0:
                print("=============SC001=============")
                print("No score for SC001")
                print("=============SC101=============")
                print("Max (101): "+ str(oneone_max))
                print("Min (101): " + str(oneone_min))
                print("Avg (101): " + str(oneone/oneone_count))
            elif oneone_count == 0:
                print("=============SC001=============")
                print("Max (001): " + str(oone_max))
                print("Min (001): " + str(oone_min))
                print("Avg (001): " + str(oone / oone_count))
                print("=============SC101=============")
                print("No score for SC101")
            else:
                print("=============SC001=============")
                print("Max (001): " + str(oone_max))
                print("Min (001): " + str(oone_min))
                print("Avg (001): " + str(oone / oone_count))
                print("=============SC101=============")
                print("Max (101): " + str(oneone_max))
                print("Min (101): " + str(oneone_min))
                print("Avg (101): " + str(oneone / oneone_count))
            break
        score = int(input("Score: "))
        if classes[2] == '1':
            oneone += score
            oneone_count += 1
            if score > oneone_max:
                oneone_max = score
            if score < oneone_min:
                oneone_min = score
        else:
            oone += score
            oone_count += 1
            if score > oone_max:
                oone_max = score
            if score < oone_min:
                oone_min = score


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
