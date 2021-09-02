def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

def reverse_string(string):
    return string[::-1]
