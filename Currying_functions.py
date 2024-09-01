def multiplyAll(int_arr,a):

    def multiply_all(a):
        return(array([x*a for x in int_arr]))

    return multiply_all(a)

print(multiplyAll([1,2,3],2))
print(multiplyAll([1,2,3],1))
print(multiplyAll([1,2,3],0))