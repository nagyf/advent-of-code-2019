start = 128392
end = 643281

def never_decrease(password):
    previous = -1
    for ch in str(password):
        if int(ch) < previous:
            return False
        previous = int(ch)

    return True

def has_duplicate_digit(password):
    str_pass = str(password)
    for i in range(0,10):
        double = '%d%d' % (i, i)
        triple = '%d%d%d' % (i, i, i)

        # Has double but doesn't have triple of the same digit
        if str_pass.find(double) != -1 and str_pass.find(triple) == -1:
            return True

    return False

def check_password(password):
    return has_duplicate_digit(password) and never_decrease(password)

def main():
    result = [password for password in range(start, end) if check_password(password)]
    print(len(result))

if __name__ == '__main__':
    main()