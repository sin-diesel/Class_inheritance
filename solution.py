from os.path import splitext


DEBUG = True


def parse_dimms(body_whl):
    assert(isinstance(body_whl, str))
    parsed = body_whl.split('x')

    if DEBUG:
        print("\n\n\nParsed values: ", parsed[0], parsed[1], parsed[2])

    try:
        parsed[0] = float(parsed[0])
        parsed[1] = float(parsed[1])
        parsed[2] = float(parsed[2])
    except ValueError:
        parsed[0] = 0
        parsed[1] = 0
        parsed[2] = 0
    return parsed


class CarBase:

    def __init__(self, car_type=None, brand=None, photo_file_name=None, carrying=None):
        if DEBUG:
            print("\n\n\n Initializing CarBase object: ")
            print("Car type: ", car_type)
            print("Brand: ", brand)
            print("Photo file name: ", photo_file_name)
            print("Carrying: ", carrying)

        self._car_type = car_type
        self._photo_file_name = photo_file_name
        self._brand = brand
        self._carriyng = carrying

    def get_photo_file_ext(self):
        splitted = splitext(self._photo_file_name)[1]

        if DEBUG:
            print("Splittex extension: ", splitted)

    def get_info(self):
        print("\n\n\n CarBase object information:")
        print("Car type: ", self._car_type)
        print("Brand: ", self._brand)
        print("Photo file name: ", self._photo_file_name)
        print("Carrying: ", self._carriyng)


class Truck(CarBase):

    def __init__(self, brand=None, photo_file_name=None, carrying=None, body_whl=None):

        super().__init__("truck", brand, photo_file_name, carrying)

        if DEBUG:
            print("Initializing truck dimensions with string: ", body_whl)
        params_list = parse_dimms(body_whl)
        self._body_length = params_list[0]
        self._body_width = params_list[1]
        self._body_height = params_list[2]

    def get_info(self):
        super().get_info()
        print("Truck dimensions: ", self._body_length, self._body_width, self._body_height)
    


