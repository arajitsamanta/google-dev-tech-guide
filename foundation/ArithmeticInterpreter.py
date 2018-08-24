
#https://codingbat.com/prob/p234011
def interpret(value, commands, args):
    n=len(commands)
    result=value
   
    for i, cmd in enumerate(commands):
        arg = args[i]
        if cmd=="+":
            result+=args[i]
        elif cmd=="-":
            result-=args[i]
        elif cmd=="*":
            result*=args[i]
        else:
            return -1
    return result;

result=interpret(1,["+","-"],[2,3]);
print("result is: ", result);