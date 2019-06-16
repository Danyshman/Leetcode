def sortArrayByParity(A):
    array_of_even_num = []
    array_of_odd_num = []
    for num in A:
        if num%2==0:
            array_of_even_num.append(num)
        else:
            array_of_odd_num.append(num)
    return array_of_even_num+array_of_odd_num