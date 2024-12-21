def kalkulyator(a, b, ishora):
    if ishora == '+':
        return a + b
    elif ishora == '-':
        return a - b
    elif ishora == '*':
        return a * b
    elif ishora == '/':
        if b == 0:
            return 0
        else:
            return a / b


n = kalkulyator(2, 4, '+')
print(n)
