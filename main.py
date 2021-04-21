def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if "capetown" == city:
        return 2500

    elif "Durban" == city:
        return 2300
    elif "JHB" == city:
        return
    elif "BFN" == city:
        return 1800
    else:
        return "location not in database "

# rental car


def rent_car_cost(days):
    car_cost = 40 * days

    if days >= 7:
        car_cost = car_cost - 50
    elif days >= 3 and days < 7:
        car_cost = car_cost - 20
    return car_cost


def trip_cost(city, days, spending_money):
    return rent_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


location = (input("where did you go: "))
days = int(input("How many days did you stay: "))
extras = float(input("How much was your extras: "))

print(trip_cost(location, days, extras))
