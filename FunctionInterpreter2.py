'''
Instructions:

Hit "GO" and enter a function into the input box

-Denote operations using the following symbols: '+' (addition), '-' (subtraction),
'*' (multiplication), '/' (division), '^' exponent
-Note that '-' denotes subtraction; use '_' as a negative sin (ex. _3*x represents -3x)
-Always enter the '*' sign - do NOT write numbers/variables/groups next to each other
with no symbol to imply multiplication (ex. write 2*(x+1), NOT 2(x+1))
-Denote trig functions using their appropriate three-letter abbreviations
(sin, cos, tan, csc, sec, cot)
-Parentheses may be used (multiple sets may be used, but not concentric sets)
-Use parentheses and the division symbol for rational functions
-Pi and Euler's number may be denoted using p and e respectively
'''

from math import sin, cos, tan, pi, e

f_string = input("Please enter function ")
x_val = float(input("Please enter x value "))

n_test = ['0','1','2','3','4','5','6','7','8','9','10','.']
t_test = ['s','c','t']

f_list = [] #Defines f_list, which will contain items representing the various "pieces" (numbers, x, operations, etc.) of the function

i = 0

while i < len(f_string): #Looks through string, examines each item, and adds it to list in the appropriate form
    if f_string[i] in n_test: #Adds multi-digit numbers (ex. 101) as list items
        num = ''
        while i < len(f_string) and f_string[i] in n_test:
            num += f_string[i]
            i += 1
        f_list.append(float(num))
    elif f_string[i] in t_test: #Adds three-letter representations of trig functions (ex. sin) as list items
        tf = ''
        for x in range(3):
            tf += f_string[i]
            i += 1
        f_list.append(tf)
    elif f_string[i] == 'p': #Replaces letter p with decimal representation of pi, adds it to list
        f_list.append(pi)
        i += 1
    elif f_string[i] == 'e': #Replaces letter e with decimal representation of Euler's number, adds it to list
        f_list.append(e)
        i += 1
    else: #Adds items not in the above categories to list (includes 'x' and operation symbols)
        f_list.append(f_string[i])
        i += 1

#print(f_list)

def f(f_list,x): #Defines function f
    i = 0
    while i < len(f_list): #Replaces 'x' with numerical value of x
        if f_list[i] == 'x':
            f_list[i] = x
        i += 1
        
    while '_' in f_list: #Eliminates '_' and makes the number immediately after it negative
        i_neg = f_list.index('_')
        f_list = f_list[:i_neg]+[-1*f_list[i_neg+1]]+f_list[i_neg+2:]
            
    #print(f_list)
    return evaluate(f_list) #Calls the evaluate function to calculate the result - returns this result
    
def evaluate(f_list): #Defines evalute function, which can compute any list using proper order of operates 
    while '(' in f_list: #Searches for parentheses (loops until all parentheses have been eliminated)
        i_open = f_list.index('(')
        i_close = f_list.index(')')
        group = f_list[i_open+1:i_close] #Creates "group," which is a new list consisting of the contents of parentheses
        #print(group)
        #print(evaluate(group))
        f_list = f_list[:i_open]+[evaluate(group)]+f_list[i_close+1:] #Calls the evaluate function for "group," and inserts the result into the list where the parentheses and their contents orginally were
        #print(f_list)
    for tf in ['sin','cos','tan','csc','sec','cot']: 
        while tf in f_list: #Looks for trig functions and evaluates all of them until none are left
            t_i = f_list.index(tf)
            if tf == 'sin': #Determines if function is sin - if so, evaluates the sin of the number following the function
                result = sin(f_list[t_i+1])
            elif tf == 'cos': #Repeates for cos and other trig functions
                result = cos(f_list[t_i+1])
            elif tf == 'tan':
                result = tan(f_list[t_i+1])
            elif tf == 'csc':
                result = 1/sin(f_list[t_i+1])
            elif tf == 'sec':
                result = 1/cos(f_list[t_i+1])
            elif tf == 'cot':
                result = 1/tan(f_list[t_i+1])
            f_list = f_list[:t_i]+[result]+f_list[t_i+2:] #Inserts result of trig calculate into list and eliminates original function and number
            #print(f_list)
    while '^' in f_list: #Evaluates all exponents
        op_i = f_list.index('^')
        result = f_list[op_i-1]**f_list[op_i+1] 
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:] #Inserts calculated result and eliminates base, exponent symbol, and power
        #print(f_list)
    while '/' in f_list: #Replaces division with multiplication by the recipricol
        i = f_list.index('/')
        f_list[i+1] = 1/f_list[i+1]
        f_list[i] = '*'
        #print(f_list)
    while '*' in f_list: #Evaluates all multiplication (same method as exponents)
        op_i = f_list.index('*')
        result = f_list[op_i-1]*f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
        #print(f_list)
    while '-' in f_list: #Replaces subtraction with addition of the opposite
        i = f_list.index('-')
        f_list[i+1] *= -1
        f_list[i] = '+'
        #print(f_list)
    while '+' in f_list: #Evaluates all addition (same method as exponents and multiplication)
        op_i = f_list.index('+')
        result = f_list[op_i-1]+f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
        #print(f_list)
    return f_list[0] #List should now contain only one number, which represents the calculated result - function returns this number
    
#f(f_list,x_val)
print(f(f_list,x_val))
