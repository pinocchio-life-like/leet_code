def convertTemperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 9/5) + 32
    return [round(kelvin, 5), round(fahrenheit, 5)]
