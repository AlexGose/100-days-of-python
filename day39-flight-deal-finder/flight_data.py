class FlightData:
    def __init__(self, price, airport_from, city_from, airport_to, city_to, departure_date, return_date):
        self.price = price
        self.airport_from = airport_from
        self.city_from = city_from
        self.airport_to = airport_to
        self.city_to = city_to
        self.departure_date = departure_date
        self.return_date = return_date

    def alert_message(self):
        message = f"Low price alert! Only ${self.price} to fly "
        message += f"from {self.city_from}-{self.airport_from} "
        message += f"to {self.city_to}-{self.airport_to} "
        message += f"from {self.departure_date} "
        message += f"to {self.return_date}."
        return message


if __name__ == '__main__':
    fd = FlightData(41, 'STN', 'London', 'SXF', 'Berlin', '2020-08-25', '2020-09-10')
    print(fd.alert_message())
    