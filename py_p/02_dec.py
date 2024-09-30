def deg(func):
    def wrapper(*args, **kwargs):
        args_value=", ".join(str(args) for i  in args  )
        return func(*args, **kwargs)
    return wrapper

def greet(name,greeting="hanji"):
    print(f"{greeting},{name}")

# greet(name='Divyanshu',greeting="hanj")
