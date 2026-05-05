# задание НЕ готово - нужно изменить методы на статические (какие?)
# перепроверить по тексту задания
# написать комментарии

class PointsForPlace:

    points = 0

    def __init__(self):
        pass

    def get_points_for_place(self, place=int):
        self.place = place
        if place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        elif place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        else:
            self.points += (101 - self.place)
            return self.points


class PointsForMeters:
    def __init__(self):
        pass

    def get_points_for_meters(self, meters: int):
        self.points = 0
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        else: 
            self.points = meters * 0.5
            return self.points


class TotalPoints(PointsForPlace, PointsForMeters):
    
    total = 0

    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)

    def get_total_points(self, meters, place):
        print(self.get_points_for_meters(meters))
        print(self.get_points_for_place(place))
        print(self.get_points_for_meters(meters) + self.get_points_for_place(place))


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
#print(total_points.get_total_points(100, 10))
