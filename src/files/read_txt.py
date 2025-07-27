from pathlib import Path


file_path = Path(r"resources\movies.txt")

# Returns the content of the file
def get_content():
    with open(file_path, 'r') as file:
        content = file.readlines()
        return content