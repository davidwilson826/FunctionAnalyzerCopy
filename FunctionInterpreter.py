f_string = "3*x^2+12*x+11"#input("Please enter function ")

n_test = ['0','1','2','3','4','5','6','7','8','9','10','.']
operations = ['+','-','*','/']

f_list = []
i = 0

while i < len(f_string):
    if f_string[i] in n_test:
        num = ''
        while i < len(f_string) and f_string[i] in n_test:
            num += f_string[i]
            i += 1
        f_list.append(float(num))
    else:
        f_list.append(f_string[i])
        i += 1

print(f_list)

def op(f_list,op_i):
    op = f_list[op_i]
    a = f_list[op_i-1]
    b = f_list[op_i+1]
    
    if op == '+':
        result = a+b
    elif op == '-':
        result = a-b
    elif op == '*':
        result = a*b
    elif op == '/':
        result = a/b
    elif op == '^':
        result = a**b
        
    f_list = f_list[:op_i]+result+f_list[:op_i+2]

def f(x):    
    i = 0
    while i < len(f_list):
        if f_list[i] == 'x':
            f_list[i] = x
        i += 1
            
    print(f_list)
    
    for i in f_list:
        if i in operations:
            op(f_list,f_list.find(i))
            
    print(f_list)
    
    
f(1)