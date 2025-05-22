class Library:
    def __init__(self):
        self.genres = set()  # Using a set to avoid duplicates

    def add_genre(self, genre):
        self.genres.add(genre)

    def show_genres(self):
        print("Library Genres:", ', '.join(self.genres))

# Example usage
lib = Library()
lib.add_genre("Fiction")
lib.add_genre("Science")
lib.add_genre("Fiction")  # Duplicate will be ignored
lib.show_genres()