# дописать вызов методов в цикле
# добавить комментарии

class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    
    def number_of_wins(victories):
        return f'Футбольных побед: {victories}'
    
    def number_of_draws(draws):
        return f'Футбольных ничьих: {draws}'

    def number_of_losses(losses):
        return f'Футбольных поражений: {losses}'
    
    def total_points(victories, draws):
        return f'Общее количество очков: {3 * victories + draws}'


class Hockey(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    
    def number_of_wins(victories):
        return f'Хоккейных побед: {victories}'
    
    def number_of_draws(draws):
        return f'Хоккейных ничьих: {draws}'

    def number_of_losses(losses):
        return f'Хоккейных поражений: {losses}'
    
    def total_points(victories, draws):
        return f'Общее количество очков: {2 * victories + draws}'

football_team = Football(2, 2, 2) 
hockey_team = Hockey(2, 2, 2)

# Вызови все методы для объектов football_team и hockey_team. 
# Используй цикл for. Названия методов при этом не должны повторяться для обоих объектов.
# Цикл for можно запустить сразу по двум элементам. 
# Будет так: for team in (football_team, hockey_team). И дальше — действия.
