from contextlib import suppress

def ignore_file_not_found(filename):
    with suppress(FileNotFoundError):
        with open(filename, 'r') as f:
            content = f.read()
            return content
    return None