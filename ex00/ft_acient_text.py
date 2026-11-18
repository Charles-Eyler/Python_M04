import sys
import typing

args = sys.argv


def open_file(arg) -> typing.IO | FileNotFoundError:
    file = open(arg, "r")
    return file


def ft_ancient_text() -> None:
    if len(args) != 2:
        return print("Usage: ft_ancient_text.py <file>")
    print("=== Cyber Archives Recovery ===")
    try:
        print("Accessing file ", args[1])
        fragment = open_file(args[1])
        print(fragment.read())
        fragment.close()
    except FileNotFoundError as e:
        return print(f"Error opening file '{args[1]}':", e)
    except PermissionError as e:
        return print(f"Error opening file '{args[1]}':", e)
    except IsADirectoryError as e:
        return print(f"Error opening file '{args[1]}':", e)


if __name__ == "__main__":
    ft_ancient_text()
