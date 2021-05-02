from fastapi import HTTPException, status


def get_length(item):
    """
    :param item: should be a string
    :return: the length of the string
    """
    # iterate over the string to count the characters
    cnt = 0
    for ch in item:
        cnt += 1
    response = dict(status_code=status.HTTP_200_OK,
                    result=cnt)
    return response


def get_generated_string(num, item):
    result = item*num
    response = dict(status_code=status.HTTP_200_OK,
                    result=result)
    return response

