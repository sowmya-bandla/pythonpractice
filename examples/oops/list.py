class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = []  # Using a list to store subjects

    def add_subject(self, subject):
        self.subjects.append(subject)

    def show_subjects(self):
        print(f"{self.name}'s Subjects: {', '.join(self.subjects)}")

# Example usage
s1 = Student("Alice")
s1.add_subject("Math")
s1.add_subject("Science")
s1.add_subject("Math")  # Lists allow duplicates
s1.show_subjects()