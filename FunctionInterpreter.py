f_string = "3*x^2+12*x"#input("Please enter function ")
#length = range(len(f_string))

#f_list = [f_string[i] for i in length]

n_test = ['0','1','2','3','4','5','6','7','8','9','10','.']
operations = ['+','-','*','/']

f_list = []
i = 0

while i < len(f_string)-1:
    if f_string[i] in n_test:
        num = ''
        while f_string[i] in n_test:
            num += f_string[i]
            i += 1
        f_list.append(float(num))
    else:
        f_list.append(f_string[i])
    
    num.append(f_string[i])
    
print(f_list)