def three_digit_seperator(num):
    ret = ''
    thousand = 1000
    while num > thousand:
        ret += str(num % 1000)
        num = int(num / 1000)
        ret += " "
    ret += str(num)
    return ret


print(three_digit_seperator(145182472105634109))
