def weather_info(temp):
    c = convert_to_celsius(temp)
    if c <= 0:
        print(f"{c} is a freezing temperature")
    else:
        print(f"{c} is an above freezing temperature")


def convert_to_celsius(temperature):
    celsius = round((temperature - 32) * (5 / 9), 2)
    return celsius

weather_info(50)