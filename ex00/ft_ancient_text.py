import sys
import typing

args = sys.argv


def open_file(arg) -> typing.IO:
    file = open(arg, "r")
    return file


def print_file_content(file) -> None:
    print("---\n")
    print(f"{file.read()}\n")
    print("---")


def ft_ancient_text() -> None:
    if len(args) != 2:
        return print("Usage: ft_ancient_text.py <file>")
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{args[1]}'")
        fragment = open_file(args[1])
        print_file_content(fragment)
        fragment.close()
        print(f"File '{args[1]}' closed")
    except Exception as e:
        return print(f"Error opening file '{args[1]}':", e)


if __name__ == "__main__":
    ft_ancient_text()
