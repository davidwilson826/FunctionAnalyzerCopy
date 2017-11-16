from math import sin, cos, tan, pi, e

f_string = input("Please enter function ")#"3*x^2-12*x+1.1+1/x"#input("Please enter function ")
x_val = float(input("Please enter x value "))

n_test = ['0','1','2','3','4','5','6','7','8','9','10','.']
t_test = ['s','c','t']

f_list = []
i = 0

while i < len(f_string):
    if f_string[i] in n_test:
        num = ''
        while i < len(f_string) and f_string[i] in n_test:
            num += f_string[i]
            i += 1
        f_list.append(float(num))
    elif f_string[i] in t_test:
        tf = ''
        for x in range(3):
            tf += f_string[i]
            i += 1
        f_list.append(tf)
    elif f_string[i] == 'p':
        f_list.append(pi)
        i += 1
    elif f_string[i] == 'e':
        f_list.append(e)
        i += 1
    else:
        f_list.append(f_string[i])
        i += 1

print(f_list)

def f(f_list,x):
    i = 0
    while i < len(f_list):
        if f_list[i] == 'x':
            f_list[i] = x
        i += 1
            
    #print(f_list)
    return evaluate(f_list)
    
def evaluate(f_list):
    while '(' in f_list:
        i_open = f_list.index('(')
        i_close = f_list.index(')')
        group = f_list[i_open+1:i_close]
        #print(group)
        #print(evaluate(group))
        f_list = f_list[:i_open]+[evaluate(group)]+f_list[i_close+1:]
        #print(f_list)
    for tf in ['sin','cos','tan','csc','sec','cot']:
        while tf in f_list:
            t_i = f_list.index(tf)
            if tf == 'sin':
                result = sin(f_list[t_i+1])
            elif tf == 'cos':
                result = cos(f_list[t_i+1])
            elif tf == 'tan':
                result = tan(f_list[t_i+1])
            elif tf == 'csc':
                result = 1/sin(f_list[t_i+1])
            elif tf == 'sec':
                result = 1/cos(f_list[t_i+1])
            elif tf == 'cot':
                result = 1/tan(f_list[t_i+1])
            f_list = f_list[:t_i]+[result]+f_list[t_i+2:]
            #print(f_list)
    while '^' in f_list:
        op_i = f_list.index('^')
        result = f_list[op_i-1]**f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
        #print(f_list)
    while '/' in f_list:
        i = f_list.index('/')
        f_list[i+1] = 1/f_list[i+1]
        f_list[i] = '*'
        #print(f_list)
    while '*' in f_list:
        op_i = f_list.index('*')
        result = f_list[op_i-1]*f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
        #print(f_list)
    while '-' in f_list:
        i = f_list.index('-')
        f_list[i+1] *= -1
        f_list[i] = '+'
        #print(f_list)
    while '+' in f_list:
        op_i = f_list.index('+')
        result = f_list[op_i-1]+f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
        #print(f_list)
    return f_list[0]
    
#f(f_list,x_val)
print(f(f_list,x_val))
