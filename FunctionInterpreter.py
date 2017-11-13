f_string = "3*x^2+12*x+11"#input("Please enter function ")

def f(f_string,x):
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
    
    i = 0
    while i < len(f_list):
        if f_list[i] == 'x':
            f_list[i] = x
            
    print(f_list)
    
    
f(f_string,1)