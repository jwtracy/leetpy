class ExamRoom:

    def __init__(self, n: int):
        self.__seat_count = n
        self.__furthest_seat = 0
        self.__seats = [False]*n
        self.__distances = [n+1]*n

    def __closest_seat(self, n: int, step: int) -> int:
        distance = 1*step
        while n+distance > 0 or n+distance < self.__seat_count:
            if self.__seats[n+distance]:
                break
            distance += step
        return abs(distance)
    
    def seat(self) -> int:
        # pick the furthest seat
        chosen = self.__furthest_seat
        self.__seats[chosen] = True
        # self.__distances[chosen] = 0
        
        print(self.__distances)
        print(self.__furthest_seat)
        
        
        print("right")
        # set the new distances to the right
        r = chosen+1
        while r < self.__seat_count:
            print("\t", i, abs(chosen-i), self.__distances[i], abs(chosen-i) == self.__distances[i])
            if abs(chosen-i) == self.__distances[i]:
                break
            self.__distances[i] = min(abs(chosen-i), self.__distances[i])
            r+=1
        print("left")
  


        # set the new distances to the left
        l = chosen-1
        while l >= 0:
            print("\t", i, abs(chosen-i), self.__distances[i], abs(chosen-i) == self.__distances[i])

            if abs(chosen-i) == self.__distances[i]:
                break
            self.__distances[i] = min(abs(chosen-i), self.__distances[i])
            l-=1
        
        furthest = 0
        # find furthest seat
        for i, d in enumerate(self.__distances):
            if d > self.__distances[furthest]:
                furthest = i

        self.__furthest_seat = furthest

        print()
        return chosen
        
    def leave(self, p: int) -> None:
        ...
