
'''need * for function to accept any number of arguments, 'args' name can be changed'''
def add(*args):
    result=0
    for n in args:
        result+=n
    return result
print(add(1,2,3,4,5,6,7,8,9))

'''unlimited key word arguments'''
def calculate(**kwargs):