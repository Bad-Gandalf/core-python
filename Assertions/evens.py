def even_number(number):
    return number % 2 == 0

def even_number_of_evens(numbers): 
    evenCount = sum([1 for n in numbers if even_number(n)])
    return False if evenCount == 0 else even_number(evenCount)
            
        
       

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([3]) == False, "One odd number"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even" 
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even" 
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")
