def greet(name: str) -> str:
    """Возвращает приветствие для указанного имени."""
    if not name:
        raise ValueError("Имя не может быть пустым")
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Складывает два числа."""
    return a + b


if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
