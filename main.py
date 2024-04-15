# Задание «Проверка логина и пароля»
def check_auth(login: str, password: str) -> str:
    if login == 'admin' and password == 'password':
        result = 'Добро пожаловать'
    else:
        result = 'Доступ ограничен'
    return result


# Задание «Количество слов»
def list_of_numbers(n: int) -> list:
    return list(range(1, n + 1))


# Задание «Победители конкурса»
def solve(receipts: list) -> tuple:
    result = receipts[2::3]
    return result, len(result)
