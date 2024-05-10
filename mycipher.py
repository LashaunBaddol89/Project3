# importing sys
import sys

# This is the main function
def main():
    # get the shift value after checking
    k = check(sys.argv)
    plain = input("plaintext: \n")
    print()
    print("Caesar Cipher output text: \n")

    caesar_txt = caesar(plain, k)

    # This first for loop get the first index value of all the lines which consists of 5 x 10 = 50
    for line_start in range(0, len(caesar_txt), 50):
        # this list has the all the elements of a line
        current_line = caesar_txt[line_start : line_start + 50]
        # this for loop makes a group of 5 letters from the line
        for block_start in range(0, len(current_line), 5):
            block = caesar_txt[line_start + block_start : line_start + block_start + 5]
            # a normal print function adds a \n or an enter after so the end="" will prevent it from doing that
            # we can tell the print function to use " " space as the end line instead of \n
            # we also join the list into a string
            print("".join(block), end=" ")
        # this print gives an enter after every line
        print()


def caesar(plain, k):
    # make the plain text into uppercase as instructed
    plain = plain.upper()
    # a list for storing the caesar txt
    caesar_txt = []
    for letter in plain:
        # check if the letters are alphabets else move forward
        if not letter.isalpha():
            continue
        # the ascii value of A is 65
        offset = 65
        # ord() gives the ascii of a letter
        # ord('A') = 65 so we can make A value to 0
        pi = ord(letter) - offset
        # we add the shift value to the pi value and do a % 26 so that if the value goes more than 26
        # it can circle back between the range 0 to 26
        ci = (pi + k) % 26
        # append the shifted text and adding the ascii value that was removed from it
        # here chr() gives the ascii characted corresponding to its number
        caesar_txt.append(chr(ci + offset))
    return caesar_txt


# check function whether the CLI argument for the caesar key K is given or not
def check(arg):
    # if only there are no two arguments or the second argument ie K is not an integer then exit
    if len(arg) != 2 or arg[1].isalpha():
        exit("Usage is as follows ==>  python caesar.py k")
    # if exits correctly then return K value
    return int(arg[1])


# call main function
if __name__ == "__main__":
    main()
