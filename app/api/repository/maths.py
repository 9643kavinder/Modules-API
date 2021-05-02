from fastapi import HTTPException, status


def helper_fibonacci(num):
    #  Taking first two fibonacci numbers as 0 and 1
    fibArray = [0, 1]
    # check is n is less than len(fibArray)
    if num <= len(fibArray):
        return fibArray[num - 1]
    else:
        temp1 = helper_fibonacci(num - 1)
        temp2 = helper_fibonacci(num - 2)
        temp_fib = temp1 + temp2
        fibArray.append(temp_fib)
        return temp_fib


def get_fibonacci(num: int):
    """
    :param num: should be an integer (num>1 and num<100).
    :return: fibonacci number at an index = num
            using Dynamic Programming Approach
            with Time Complexity = O(n)
    """

    result = helper_fibonacci(num)
    response = dict(status_code=status.HTTP_200_OK,
                    result=result)
    return response


def helper_factorial(num):
    return 1 if (num == 1 or num == 0) else num * helper_factorial(num-1)


def get_factorial(num: int):
    """
    :param num: should be a non-negative integer
    :return: the multiplication of all integers smaller than
            or equal to num.
    """

    result = helper_factorial(num)
    response = dict(status_code=status.HTTP_200_OK,
                    result=result)
    return response
