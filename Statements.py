"""
Write the program "99 Bottles of Beer on the Wall" using a while loop. 
Be mindful to change the word 'bottles' to 'bottle' when down to the last one. 
You must do the full 99 bottles; the sample shows the last 3 verses.
"""
# Type out while loop for 99 bottle of beer on the wall
count = 100
while count > 0:
    if count == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer")
        print("1 bottle of beer")
    else:
        print(f"{count} bottles of beer on the wall")
        print(f"{count} bottles of beer")
        print("Take one down, pass it around")
    count -= 1