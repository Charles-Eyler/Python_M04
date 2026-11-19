import sys
import typing

args: list[str] = sys.argv


def open_file(arg, mode) -> typing.IO[typing.Any]:
    file = open(arg, mode)
    return file


def print_file_content(file) -> None:
    print("---\n")
    print(f"{file.read()}\n")
    print("---")


def transform_data(data) -> str:
    buffer: str = ""
    for line in data.splitlines():
        buffer = buffer + line + "#\n"
    return (buffer)


def print_buffer_content(buffer) -> None:
    print("---\n")
    print(f"{buffer}")
    print("---")


def ft_stream_management() -> None:
    if len(args) != 2:
        return print("Usage: ft_ancient_text.py <file>")
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        print(f"Accessing file '{args[1]}'")
        fragment: typing.IO[typing.Any] = open_file(args[1], "r")
        print_file_content(fragment)
        fragment.close()
        print(f"File '{args[1]}' closed")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file "
                         f"'{args[1]}': {str(e)}\n")
        return
    try:
        print("Transform data:")
        fragment = open_file(args[1], "r")
        line = fragment.read()
        buffer: str = transform_data(line)
        print_buffer_content(buffer)
        fragment.close()
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_file: str | typing.Any = sys.stdin.readline().strip()
        if new_file == "":
            return print("Not saving data")
        new_data: typing.IO[typing.Any] = open(new_file, "w+")
        new_data.write(buffer)
        sys.stdout.write(f"File '{new_file}' closed\n")
        print(f"Data saved in file '{new_file}'")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file "
                         f"'{new_file}': {str(e)}\n")
        return


if __name__ == "__main__":
    ft_stream_management()

