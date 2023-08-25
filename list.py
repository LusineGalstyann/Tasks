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
# You'll be given a list of two strings, and each will contain exactly one colon (":") in the middle (but not at beginning or end). The length of the strings, before and after the colon, are random.
#
# Your job is to return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.
#
# Examples
# ["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
# ["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]



def tail_swap(strings):
    st1 = strings[0].split(':')
    st2 = strings[1].split(':')
    return (([st1[0] + ':' + st2[1]], [st2[0] + ':' + st1[1]]))

#
# list1=(['abc:123', 'cde:456'])
# print(tail_swap(list1))
# list2=(['a:12345', '777:xyz'])
# print(tail_swap(list2))