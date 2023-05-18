PASSWORD = '12345'

#decorators begin
def password_required(func):
    def wrapper():
        password = input('password?')

        if password == PASSWORD:
            return func()
        else:
            print('Contrasena no es correcta')
    return wrapper

def upper(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result.upper()
    
    return wrapper
#decorators end

@password_required
def needs_password():
    print('Nice pass')

@upper
def say_my_name(name):
    return 'Hola, {}'.format(name)


if __name__ == '__main__':
    needs_password()
    say_my_name('Carlos')