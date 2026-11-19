import sys
import typing

args = sys.argv


def open_file(arg, mode) -> typing.IO:
    file = open(arg, mode)
    return file


def print_file_content(file) -> None:
    print("---\n")
    print(f"{file.read()}\n")
    print("---")


def transform_data(data):
    buffer = ""
    for line in data.splitlines():
        buffer = buffer + line + "#\n"
    return (buffer)


def print_buffer_content(buffer) -> None:
    print("---\n")
    print(f"{buffer}")
    print("---")


def ft_archive_creation() -> None:
    if len(args) != 2:
        return print("Usage: ft_ancient_text.py <file>")
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{args[1]}'")
        fragment = open_file(args[1], "r")
        print_file_content(fragment)
        print(f"File '{args[1]}' closed")
    except Exception as e:
        return print(f"Error opening file '{args[1]}':", e)
    try:
        print("Transform data:")
        fragment = open_file(args[1], "r")
        line = fragment.read()
        buffer = transform_data(line)
        print_buffer_content(buffer)
        new_file = input("Enter new file name (or empty):")
        if new_file == "":
            return print("Not saving data")
        new_data = open(new_file, "w")
        new_data.write(buffer)
        new_data = open(new_file, "r")
        print_file_content(new_data)
        new_data.close()
        print(f"File '{new_file}' closed")
        print(f"Data saved in file '{new_file}'")
    except Exception as e:
        return print(f"Error opening file '{new_file}':", e)


if __name__ == "__main__":
    ft_archive_creation()
