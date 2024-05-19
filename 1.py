def funcTest1 (lst):
    return sorted(set(lst))        
                 
main_lst = [10, 4, 8, 10, 4, 5, 1, 5, 4, 5, 6, 3, 4, 5, 6, 10]

print(funcTest1(main_lst))