"""
Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#   #
#    #
#     #
"""
#r for row and c for column
for r in range(6):
    for c in range(r+2):    
        if c == 0 or c == r + 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()  # Move to the next line after each row
