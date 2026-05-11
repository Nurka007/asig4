import os


class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def check_file(self):
        if os.path.exists(self.filepath):
            print(f"File found: {self.filepath}")
        else:
            print(f"File NOT found: {self.filepath}")
            raise FileNotFoundError(f"{self.filepath} does not exist.")

    def create_output_folder(self, folder="output"):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")
        else:
            print(f"Folder already exists: {folder}")