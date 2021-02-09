

def bus_task(age, student):
    price = 4.00
    if age < 3 or age >= 65:
        price = 0
    elif student and age < 19:
        price = price/2
    return price


def speeding_ticket(speed, speed_limit):
    if speed > speed_limit+10:
        return True, True
    elif speed > speed_limit:
        return True, False
    return False, False


def delivery_task(value_of_goods, miles):
    if miles <= 10 and value_of_goods >= 100:
        return 0
    elif miles <= 10:
        return 5
    elif miles < 20:
        return 10
    elif miles < 30:
        return 15

    return (miles-30)*0.5 + 15
