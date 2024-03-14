def str_upper(s: str):
    """возвращает строку с заглавными буквами"""
    if s.isalpha():
        return s.upper()
    return s


def str_title(s: str):
    """возвращает строку с заглавными первыми буквами в каждом слове"""
    if s.isalpha():
        return s.title()
    return s
