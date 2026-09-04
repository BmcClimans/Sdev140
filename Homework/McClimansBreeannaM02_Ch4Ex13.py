"""
Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#   #
#    #
#     #
"""

for r in range(6):
    for c in range(r+1):
        if c == 0 or c == r:
            print("#", end="")
        else:
            print(" ", end="")
    print()  # Move to the next line after each row