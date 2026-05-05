class Movies: 

    def __init__(self):
        self.movies = [] # инициализировал пустой список в суперклассе через конструктор
    
    def add_movie(self, movie): # добавил метод add_movie: добавляет фильм в конец списка
        self.movies.append(movie) 
        return self.movies
    
class Comedy(Movies):

    def add_movie(self, movie): # переопределил метод для подкласса: возвращает список комедий в виде f-строки
        self.movies = super().add_movie(movie) 
        return f'Комедии: {self.movies}' 

class Drama(Movies):

    def add_movie(self, movie): # переопределил метод для подкласса: возвращает список драм в виде f-строки
        self.movies.append(movie)
        return f'Драмы: {self.movies}'


comedy = Comedy()
drama = Drama()

print(comedy.add_movie('Большой куш'))
print(drama.add_movie('Оружейный барон'))
