class FileExistsError(Exception):
    def __init__(self, filename):
        super().__init__(f"File '{filename}' already exists.")
        self.filename = filename

def create_file_safely(filename):
    try:
        with open(filename, 'w') as f:
            pass
    except FileExistsError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")