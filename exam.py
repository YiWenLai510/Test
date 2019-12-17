def Q1_a_reverse_string_1(input):
    output = ""
    for i in range(len(input)):
        output += input[len(input)-1-i]
    return output
def Q1_b_reverse_string_2(input):
    output=""
    tmp = input.split()
    print(tmp)
    for z in range(len(tmp)):
        item = tmp[z]
        x = ""
        for i in range(len(item)):
            x += item[len(item)-1-i]
        output += x
        if z < len(tmp)-1:
            output += " "
    return output
def Q2(x):
    output=[]
    for i in range(x):
        if (i+1) %3 == 0 and (i+1) %5 == 0:
            output.append(i+1) 
        elif (i+1) %3 != 0 and (i+1) %5 != 0:
            output.append(i+1)
    return output

'''print(Q1_a_reverse_string_1("abcdefsa"))
print(Q1_b_reverse_string_2("Ivy is cool"))
print(Q2(30))'''