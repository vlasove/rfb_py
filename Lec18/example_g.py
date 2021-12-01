def parse(**kwargs):
    print("Kwargs:", kwargs)
    print("Kwargs type:", type(kwargs))
    for k, v in kwargs.items():
        print(k, v)


parse(name="Vova", last_name="Petrov", age= 30)
parse(weight = 100, height= 300, balance = "100 USD")


def strange(*args, **kwargs):
    print(args)
    print(kwargs)

strange(10, 20, 30, 40, "asd", name = "F", age = 20)