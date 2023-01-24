def sumNumDigits(num):
    if num >= 10:
        return((num % 10)+sumNumDigits(num // 10))
    else:
        return(num)
