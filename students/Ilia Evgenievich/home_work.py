def calculator(args, operation):
    rezult = 0
    if operation == "minus":
        for a in args:
           rezult -= a
    elif operation == "multiply":
        rezult = 1
        for a in args:
            rezult = rezult * a
    elif operation == "division":
        rezult = args[0]
        for a in args[1:]:
            if a == 0:
                print('divisoin by zero')
            else:
                rezult = rezult / a
    elif operation == "":
        for a in args:
            rezult += a
    elif operation == "add":
        for a in args:
            rezult += a
    else:
        print("incorrect input")
        rezult = calculator(args, input())
    return rezult



def to_int(list):
    int_list = []
    for elem in list:
        int_list.append(int(elem))
    return int_list


print(calculator(to_int(input().split()), input()))
