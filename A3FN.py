def add(number):
    result = 0
    for value in number:
        result += value
    return result
    
Output = add([8,2,3,0,7])
print(Output)