import csv

MOVIE_FILE = "movies.csv"


def load_movies(filename):
    movies = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                movies.append({
                    "title": row["title"].strip(),
                    "year": row["year"],
                    "genres": [g.strip().lower() for g in row["genres"].split("|")],
                    "director": row["director"].strip().lower(),
                    "actors": [a.strip().lower() for a in row["actors"].split("|")],
                    "length": int(row["length"])
                })
            except:
                # Skip bad rows
                continue

    return movies


def print_movies(movies):
    if not movies:
        print("No movies found.")
        return

    for i, m in enumerate(movies, 1):
        print(
            f'{i}. "{m["title"]}" ({m["year"]}) | '
            f'Genres: {"|".join(m["genres"])} | '
            f'Director: {m["director"].title()} | '
            f'Length: {m["length"]} min'
        )


def search_movies(movies):
    results = movies[:]

    print("\nChoose filters (comma separated):")
    print("1. Genre")
    print("2. Director")
    print("3. Actor")
    print("4. Length")

    choices = input("Your choice: ").split(",")

    for choice in choices:
        choice = choice.strip()

        if choice == "1":
            genre = input("Enter genre: ").lower()
            results = [
                m for m in results
                if genre in " ".join(m["genres"])
            ]

        elif choice == "2":
            director = input("Enter director: ").lower()
            results = [
                m for m in results
                if director in m["director"]
            ]

        elif choice == "3":
            actor = input("Enter actor: ").lower()
            results = [
                m for m in results
                if actor in " ".join(m["actors"])
            ]

        elif choice == "4":
            min_len = input("Min length (blank = none): ")
            max_len = input("Max length (blank = none): ")

            if min_len:
                results = [m for m in results if m["length"] >= int(min_len)]
            if max_len:
                results = [m for m in results if m["length"] <= int(max_len)]

    print("\nResults:")
    if not results:
        print("No movies match those filters. Try removing one.")
    else:
        print_movies(results)


def main():
    movies = load_movies(MOVIE_FILE)

    print("\n🎥 Movie Recommendation Program")
    print("Search movies by genre, director, actor, and length.\n")

    while True:
        print("\nMain Menu")
        print("1. Search / Get Recommendations")
        print("2. Print Full Movie List")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_movies(movies)
        elif choice == "2":
            print_movies(movies)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
