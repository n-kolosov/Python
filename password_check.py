password = input("Введите пароль: ")

def test_password(p):
    def deco(f):
        if p == "10":
            return f
        else:
            return lambda: "Доступ закрыт"
    return deco

@test_password(password)
def func():
    return "Доступ открыт"
print(func())