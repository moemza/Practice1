
def filter_numbers(num1, num2):
    """Create a Python program that returns all the numbers from 0-9 except for the 
    two numbers that the user has inputted.

    e.g. If a user inputs: 3 and 6

    The program will return: 1 2 4 5 7 8 9

    Args:
        num1 (int): The first number to exclude
        num2 (int): The second number to exclude
    """
    numbers = []
    for i in range(10):
        if i != num1 and i != num2:
            numbers.append(str(i))
    return ' '.join(numbers)
        

def star_conversion(word, index):
    """Create a program that will turn the letter at the entered index into an asterisk.

    e.g.The given word: lovely
        The given index: 3

        The program must return: lo*ely

    Args:
        word (string): The word to be iterated 
        index (int): The index to be replaced
    """
    new_word = []
    for i in word:
        new_word.append(i)
    if len(new_word) < index:
        print("Index out of range")
    else:
        new_word[index] = "*"    
        return ''.join(new_word)

def find_exponent(a, n):
    """Create a program to find an integer exponent x such that a^x = n.

    e.g. If user inputs: a=2 n=4

    The program will return: x=2

    Args:
        a (int): The base int
        n (_type_): The solution
    """
    
    if a <= 1 or n < 1:
        return None
    
    x = 0
    total = 1 # anything to the exponent 0 = 1
    while total < n:
        x = x + 1
        total = total * a
    if total == n:
        return f"x={x}"  # We found the exponent
    else:
        return None
    

def reverse_cases(word_list):
    """Create a program to reverse the case of all strings. For those strings, which contain no letters, reverse the strings.

    Args:
        word_list (list): List to be reversed
    """
    reversed_list = [] 
    
    for word in word_list:
        if any(char.isalpha() for char in word):  # Check for letter
            reversed_list.append(word.swapcase()) 
        else:
            reversed_list.append(word[::-1]) 
    
    return reversed_list 

def month_days(month):
    """Create a program that returns the number of days in the month that the user inputs.

    e.g. If a user inputs: January

    The program will return: 31 days

    Args:
        month (str): month
    """
    
    month_days = {
        "january": 31,
        "february": 28,  
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }

   
    month = month.lower()

    # Check if the month is valid and return the number of days
    if month in month_days:
        month_day = month_days.get(month)
        #month = month.capitalize()
        return f"{month_day} days"
    else:
        return "Invalid month!"


def remove_duplicates(list):
    """Create a program to remove duplicates from a list of integers, preserving order.

    Args:
        list (list): A list that will contain duplicate items.

    Input:
[1, 3, 4, 10, 4, 1, 43]
Output:
[1, 3, 4, 10, 43]
Input:
[10, 11, 13, 23, 11, 25, 23, 76, 99]
Output:
[10, 11, 13, 23, 25, 76, 99]    
    """
    final_list = []
    for i in list:
        if i not in final_list:
            final_list.append(i) 
        else:
            continue
    return final_list


def fibonacci(n):
    """
    Create a program that returns a list, of n-length, of fibonacci numbers.

    e.g. For the argument n=4

    The program will return: 0 1 1 2

    Args:
        n (int): The expected list range
    """
    fib_list = [0,1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [fib_list]
    else:
        for i in range(2,n):
            sum = fib_list[i-1] + fib_list[i-2]
            fib_list.append(sum)
    
    return fib_list
        


def prime_words(sentence):
    """Create a program to find the string consisting of all the words whose lengths are prime numbers.

    Input:
The quick brown fox jumps over the lazy dog.
Output:
The quick brown fox jumps the
Input:
Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later.
Output:
Omicron Effect: Foreign Flights Won't On Dec 15,

    Args:
        sentence (str): _description_
    """
   

    list_words = ' '.split(sentence)
    for i in list_words:
        lenword = len(i) 
            list_words
    if lenword > 1: 
             for x in range (2, lenword): 
                 if lenword % x == 0:
                                           
            
         else: 
            return False 

    


    
def shift_decimals(test_int, decimal_shift):
    """Create a program to shift the decimal digits n places to the left, wrapping the extra digits around. 
    If the shift > the number of digits in n, reverse the string.
Input:
n = 12345 and shift = 1
Output:
Result = 23451
Input:
n = 12345 and shift = 2
Output:
Result = 34512
Input:
n = 12345 and shift = 3
Output:
Result = 45123
Input:
n = 12345 and shift = 5
Output:
Result = 12345
Input:
n = 12345 and shift = 6
Output:
Result = 54321

    Args:
        test_int (int): int of 5 values
        decimal_shift (int): num of decimal shifts
    """
print(filter_numbers(2, 5))
print(star_conversion("Moemedi",5))
print(find_exponent(2,9))
print(reverse_cases(['The','shee','dogs']))
print(month_days("february"))
print(remove_duplicates([1, 3, 4, 10, 4, 1, 43]))
print(fibonacci(10))
