from math import sin, cos, tan, csc, sec, cot

f_string = input("Please enter function ")#"3*x^2-12*x+1.1+1/x"#input("Please enter function ")

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
        trig = ''
        for x in range(3):
            trig += f_string[i]
            i += 1
        f_list.append(trig)
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
            
    print(f_list)
    
    while 'sin' in f_list:
        t_i = f_list.index('sin')
        result = sin(f_list[t_i+1])
        f_list = f_list[:t_i]+[result]+f_list[t_i+2:]
    
    while '^' in f_list:
        op_i = f_list.index('^')
        result = f_list[op_i-1]**f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
        print(f_list)
    while '/' in f_list:
        i = f_list.index('/')
        f_list[i+1] = 1/f_list[i+1]
        f_list[i] = '*'
        print(f_list)
    while '*' in f_list:
        op_i = f_list.index('*')
        result = f_list[op_i-1]*f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
        print(f_list)
    while '-' in f_list:
        i = f_list.index('-')
        f_list[i+1] *= -1
        f_list[i] = '+'
        print(f_list)
    while '+' in f_list:
        op_i = f_list.index('+')
        result = f_list[op_i-1]+f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
        print(f_list)
    
f(f_list,2)