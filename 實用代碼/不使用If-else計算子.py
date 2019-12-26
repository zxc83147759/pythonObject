import operator


def operation(str1, num1, num2):
    action = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.truediv,
        '/': operator.mul,
        '**': operator.pow,
    }
    return action[str1](num1, num2)


print(operation('-', 50, 20))
