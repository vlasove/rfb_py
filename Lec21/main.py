def add(a,b):
                    return a +                b

def sub(c, c1):



 return c + c1


def mult(x,y         ):
    return                         x                        *                     y


def деление(o, o2):
 return o // o2


def main():
    a,b = int(input().strip()), int(input().strip())
    result = add(a,b) + add(b,a) + sub(add(a,a), mult(b,b)) - деление(b,a) ** 2 + add(a,b) + add(b,a) + sub(add(a,a), mult(b,b)) - деление(b,a) ** 2
    print(result)

if __name__ == '__main__':
    main() 