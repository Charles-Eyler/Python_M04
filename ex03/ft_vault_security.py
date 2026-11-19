def secure_archive(filename: str, mode: str = "r",
                   add_str: str = "42 is awesome") -> tuple:
    try:
        with open(filename, mode) as file:
            if mode == "w+" or mode == "w":
                file.write(add_str)
            success = (True, file.read())
            return success
    except Exception as e:
        error = (False, str(e))
        return error


if __name__ == "__main__":
    print(f"Using {secure_archive.__name__} to read from a nonexistent file:")
    print(f"{secure_archive("IDoNotExist")}\n")
    print(f"Using {secure_archive.__name__} to read from a inaccessible file:")
    print(f"{secure_archive("secured.txt")}\n")
    print(f"Using {secure_archive.__name__} to read from a regular file:")
    data = secure_archive("data_fragment.txt")
    print(f"{data}\n")
    print(f"Using {secure_archive.__name__} to write previous"
          " content to a new file:")
    secure_archive("new_data_fragment.txt", "w", 
                   "Content successfully written to file")
    print(f"{secure_archive("new_data_fragment.txt", "r",)}\n")
