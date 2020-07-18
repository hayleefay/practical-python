# bounce.py
#
# Exercise 1.5

height = 100
ratio = 3/5
bounce_number = 0

while bounce_number < 10:
    # keep track of bounce number
    bounce_number += 1
    # take the height and multiply by ratio
    height = height * ratio

    print(bounce_number, round(height, 4))



