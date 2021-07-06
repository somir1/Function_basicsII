def countdown(number):
    output = []
    for i in range(number,-1,-1):
        output.append(i)
    return output

print(countdown(200))

def print_A_return(list):
    print(list[0])
    return list[1]

print(print_A_return([3,5]))

def first_P_len(list):
    return list[0]+ len(list)

print(first_P_len([2,6,9,8,1,5]))

def VGS(list):
    if len(list) < 2:
        return False
    newlist = []
    count = 0
    for i in range(0, len(list)):
        if list[i] > list[1]:
            newlist.append(list[i])
    print(len(newlist))
    return newlist

print(VGS([5,6,9,7,23,1]))
print(VGS([6]))

def lAv(n1, n2):
    output = []
    for i in range(0,n1):
        output.append(n2)
    return output

print(lAv(4,7))
print(lAv(6,2))