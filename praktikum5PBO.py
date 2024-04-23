"""""
class FilmFavorit:
    def __init__(self):
        self.list_film = []

    def tambah_film(self, film):
        self.list_film.append(film)

    def tampilkandaftar(self):
        print("\n===========DAFTAR FILM FAVORIT===========")
        for i, film in enumerate(self.list_film, start=1):
            print(f"{i}.) {film}")


def film():
    daftar_film = FilmFavorit()

    print("----------ELKOM 1---------")
    for i in range(5):
        film = input("film favorit ke-{}: ".format(i+1))
        daftar_film.tambah_film(film)

    daftar_film.tampilkandaftar()

if __name__ == "__main__":
    film()
"""
class Movie:
    def __init__(self, title, release_year, director, order):
        self.title = title
        self.release_year = release_year
        self.director = director
        self.order = order

    def display_info(self):
        print(f"Film favorit ke-{self.order}:")
        print(f"Judul: {self.title}")
        print(f"Tahun Rilis: {self.release_year}")
        print(f"Sutradara: {self.director}")

# List untuk menyimpan objek Movie
daftar_film = []

# Data film favorit
film_data = [
    {"title": "Kung fu panda 1", "release_year": 2008, "director": "Mark Osborne"},
    {"title": "Kung fu panda 2", "release_year": 2011, "director": "Mark Osborne"},
    {"title": "Kung fu panda 3", "release_year": 2016, "director": "Mark Osborne"},
    {"title": "Kung fu panda 4", "release_year": 2024, "director": "Mark Osborne"},
    {"title": "Toy story 4", "release_year": 2019, "director": "John Lasseter"}
]

# Memasukkan data film ke dalam daftar_film
for i, data in enumerate(film_data, start=1):
    movie = Movie(data["title"], data["release_year"], data["director"], i)
    daftar_film.append(movie)

# Menampilkan informasi film
print("----------ELKOM 2----------")
for film in daftar_film:
    film.display_info()
    print("==============")