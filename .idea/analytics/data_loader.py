import csv

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.students = []

    def load(self):
        with open(self.filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.students = [row for row in reader]
        print(f"Loaded {len(self.students)} students from {self.filepath}")

    def preview(self, n=5):
        print(f"\n--- Preview: first {n} rows ---")
        for row in self.students[:n]:
            print(row)
        print("-------------------------------\n")