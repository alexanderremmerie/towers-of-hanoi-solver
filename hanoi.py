# get user input(rings)
user_input = int(input("How many rings are there? \n"))

 # start of process
print("starting...")

 # define rings
rings = user_input
print("rings: " + str(rings))

# define the main_string
main_string = "1"

for number in range(2, rings + 1):
    main_string = main_string + "," + str(number) + "," + main_string
# main_string to array
main_string = main_string.split(",")
#
print("minimum amount of moves: " + str(len(main_string)))

# even or uneven amount of rings?
if (rings % 2) == 0:
    even = True
else:
    even = False

# define three dimensional main_list
a = [[0 for x in range(3)] for y in range(rings + 1)]

# initialise main_list
for x in range(1, rings + 1):
    a[x][1] = x

    if even == True:
        if (x % 2) == 0:
            a[x][2] = 3
        else:
            a[x][2] = 2
    else:
        if (x % 2) == 0:
            a[x][2] = 2
        else:
            a[x][2] = 3

# main loop start
print("best solution: \n")

# main loop
for x in range(1, len(main_string) + 1):
    # define  current piece
    piece = int(main_string[x - 1])

     # telling wich move it is doing and move piece
    print("move: " + str(x) + "    move piece " + str(piece) + " to tower " + str(a[piece][2]))

    # adjusting the values of the pieces
    if even == True:
        if (x % 2) == 0:
            a[piece][2] = a[piece][2] - 1
        else:
            a[piece][2] = a[piece][2] + 1
    else:
        if (x % 2) == 0:
            a[piece][2] = a[piece][2] + 1
        else:
            a[piece][2] = a[piece][2] - 1

    # making sure the value is 1, 2 or 3
    if a[piece][2] == 4:
        a[piece][2] = 1
    if a[piece][2] == 0:
        a[piece][2] = 3

 # end
print("\nending...")

