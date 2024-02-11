lst_numbers = [] #create a list of the numbers inputed by the user

while True:
    
    try:
        number = int(input("Please, enter a number (-1 to exit):"))
        if number == -1:
            break
        lst_numbers.append(number) # Append the item to the list 
        
    except ValueError: # Handles non numerical values
        print("Please, enter a numerical value!")

if len(lst_numbers)>0: # Check list size to avoid a ZeroDivisionError: division by zero when the user first enters -1.

    total = sum(lst_numbers)
    lst_len = len(lst_numbers)
    lst_avg = total/lst_len # Calculates the average
    print(f"The value of the average of the list of numbers inputed by the user is {lst_avg}.")         

else:
    print("You provided no numbers! Please, enter a numerical value!")
    
# ######################################################################################################
# Dear Alfred Ndlovu, unfortunately I could not reproduce the NameError you mentioned in the review.   #
# The lst_numbers variable you mentioned on line 9, is declared in the first line of the code.         #
########################################################################################################
 