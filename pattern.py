# The code output a star pattern using an if-else statement
# in combination with a single for loop.

pattern = ""
count_up = 9

for num in range(9): # The range is nine because we must have to print a star pattern with nine lines.
      
    if num <5: # 5 is the transition point to start the decreasing order.
        pattern += "*" # To increase the star_count.
    else:
        pattern = "*" * ( 9 - num ) # To decrease the star_count.
    
    print(f"{pattern}") # Print the star pattern.