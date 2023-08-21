# task 1

# to implement a difference function, which subtracts one list from another and returns the result.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]
# It should remove all values from list a, which are present in list b keeping their order.

def array_diff(a, b):
    rezult = []
    for i in a:
        if i not in b:
            rezult.append(i)
    return rezult
#task 2
def tail_swap(strings):
    ind1=strings[0].index(":")
    print(ind1)
    ind2=strings[1].index(":")
    print(ind1)
    st1=strings[0][:ind1]
    st2=strings[0][ind1:]
    st3=strings[1][:ind2]
    st4=strings[1][ind2:]
    list([st1+st3],[st2+st4])
    pass
listss=(["as:bd","asdyy:123"])
tail_swap(listss)