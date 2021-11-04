def interpret(value, commands, args):

    result = value

    for i in range(len(commands)):
        if commands[i] == "+":
            result += args[i]
        elif commands[i] == "-":
            result -= args[i]
        elif commands[i] == "*":
            result *= args[i]
        else:
            return -1

    return result


print(interpret(1, ['+', '*'], [1, 3]))
