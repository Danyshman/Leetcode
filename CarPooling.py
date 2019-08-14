def carPooling(trips, capacity):
    unique_points = set()
    for trip in trips:
        unique_points.add(trip[1])
        unique_points.add(trip[2])
    unique_points = list(unique_points)
    unique_points.sort()
    total_passengers = 0
    for point in unique_points:
        if total_passengers > capacity:
            return False
        for trip in trips:
            if trip[1] == point:
                total_passengers += trip[0]
            if trip[2] == point:
                total_passengers -= trip[0]
    return True


print(carPooling([[2,2,7],[9,5,6],[10,1,7],[3,3,6],[2,1,4]], 24))