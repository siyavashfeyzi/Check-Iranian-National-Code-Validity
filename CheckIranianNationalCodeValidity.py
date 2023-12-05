# Get the national code
import re
nationalCode = input("insert your national code: ")

if len(nationalCode) == 10:
    if nationalCode in ('1111111111', '2222222222', '3333333333', '5555555555',
                        '6666666666', '7777777777', '8888888888', '9999999999'):
        print('Wrong!!!')
    else:
        nationalCodeNumbers = [x for x in nationalCode]
        # natonal Code is 10 number like be that
        # XXXXXXXXXA
        check = int(nationalCodeNumbers[9])
        s = (
            int(nationalCodeNumbers[0])*10 + int(nationalCodeNumbers[1])*9 + int(nationalCodeNumbers[2])*8 +
            int(nationalCodeNumbers[3])*7 + int(nationalCodeNumbers[4])*6 + int(nationalCodeNumbers[5])*5 +
            int(nationalCodeNumbers[6])*4 + int(nationalCodeNumbers[7])*3 + int(nationalCodeNumbers[8])*2)
        c = s % 11
        if (c < 2 and check == c) or (c >= 2 and check == abs(11 - c)):
            print("Correct!!")
        else:
            print('Wrong!!!')
else:
    print('Wrong!!!')

# another solution from https://gist.github.com/ebraminio/5292017


def is_valid_iran_code(input: str) -> bool:
    if not re.search(r'^\d{10}$', input):
        return False
    check = int(input[9])
    s = sum(int(input[x]) * (10 - x) for x in range(9)) % 11
    return check == s if s < 2 else check + s == 11
