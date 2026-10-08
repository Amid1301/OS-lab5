def greet(name: str) -> str:
    """Возвращает приветствие для указанного имени."""
    if not name:
        raise ValueError("Имя не может быть пустым")
    return f"Hello, {name}!"
