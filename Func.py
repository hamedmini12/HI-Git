def shomenu(menu: dict) -> str:
    """It takes a dictionary and displays the key-value 
    pairs in an organized manner in the output.

    Args:
        menu (dict):

    Returns:
        str:
    """
    for key, value in menu.items():
        print(f"{key} : {value}")


def isvalid(value: str, pattern: str) -> bool:
    """It takes a value and a pattern,
     and returns `true` if the value matches the pattern.

    Args:
        value (str): can use for names numbers or ...
        pattern (str): Regex pattern (r"[a-zA-Z]+") 

    Returns:
        bool: true | false
    """
    from re import fullmatch

    if fullmatch(pattern, value):
        return True
    else:
        return False


def make_Dictionary(Iterable: list | tuple | str) -> dict:
    """

    Args:
        Iterable (list | tuple | str):The iterable items you want to convert into a dictionary.

    Raises:
        er: If the value is not navigable

    Returns:
        dict:
    """
    try:
        for _ in Iterable:
            pass
    except Exception as er:
        raise er

    main_dict = {}
    for index, value in enumerate(Iterable):
        main_dict.setdefault(index + 1, value)
    return main_dict

# kodo sher