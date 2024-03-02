# Count how many sailors fall into the water in the given
# boundaries and given steps taken by the sailors.


from random import randint

size = int(input("Enter the size: "))       # Boundaries
step = int(input("Enter the number of steps: "))
sailors = int(input("Enter the number of sailors: "))

safe = fall = 0            # Drunkers inside and out of the boundaries
for i in range(sailors):   # Number of drunken sailors
    sum_x = sum_y = 0      # Value of x and y
    for j in range(step):     # Number of steps taken by sailors
        rn = randint(1, 4)    # 1,2,3,4 stand for 4 directions seperately
        if rn == 1:
            x = -1            # move one step left in the X direction
            sum_x += x
        elif rn == 2:
            x = 1             # move one step right in the X direction
            sum_x += x
        elif rn == 3:
            y = -1            # move one step downwords in the Y direction
            sum_y += y
        else:
            y = 1             # move one step upwords in the Y direction
            sum_y += y

    # Between the boundaries in the X and Y directions
    if -1*size <= sum_x <= size and -1*size <= sum_y <= size:
        safe += 1            # Numbers of drunk sailors inside the boundary
    else:
        fall += 1            # Numbers of drunk sailors out of the boundary
        rate = round(fall/sailors, 4)*100

print(f"\nOut of {sailors} drunk sailors, {fall}({rate}%) fell into water.")
