""" 

    demonstrate global variables
"""

PI = 3.14 # Global because outside of functions in scope everywhere



def main():
    global PI 
    area = PI * (4 *4)
    print(f"area is {area: ,.1f}")

main()