def count_case_letters(simvol):
    upper_cnt = sum(1 for char in simvol if char.isupper())  
    lower_cnt = sum(1 for char in simvol if char.islower())
    return upper_cnt, lower_cnt

string = input("Enter the string: ")
upper, lower = count_case_letters(string)

print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
