"""
Open sales_totals in read mode (Download the start file)
Read each line in a loop
Strip newline and convert to float
Add to running total
Count the lines
Format and print each number
Print the total, count, and average
Use a main() function
Use try and except for errors
"""

def main():
    # initialize variables
    total = 0.0      
    count = 0        

    try:
        # open the file in read mode
        with open("sales_totals.txt", "r") as file:
            lines = file.readlines()  

            # convert to float
            for line in lines:
                number = float(line.strip())  
                print(f"{number:.2f}")        
                total += number               
                count += 1                    

        # print results after loop
        print(f"\nTotal: {total:.2f}")
        print(f"Count: {count}")
        print(f"Average: {total / count:.2f}")

    except IOError:
        # error in file 
        print("An IOError occurred.")

main()