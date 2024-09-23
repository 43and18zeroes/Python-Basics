def read_file_safely(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"Permission denied to access '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")