from os.path import splitext


DEBUG = True


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
            print("Initializing truck dimensions with list: ", body_whl)
            
        if type(body_whl[0]) == float and type(body_whl[1]) == float and type(body_whl[2]) == float:
            if DEBUG:
                print("\n\n\nCorrect dimensions input.")
            self._body_length = body_whl[0]
            self._body_width = body_whl[1]
            self._body_height = body_whl[2]
        else:
            self._body_length = 0
            self._body_width = 0
            self._body_height = 0

    def get_info(self):
        super().get_info()
        print("Truck dimensions: ", self._body_length, self._body_width, self._body_height)


    body_whl = property()

    @body_whl.setter
    def body_whl(self, data):  # check if list contains valid float numbers
        if DEBUG:
            print("\n\n\nSetting dimensions property...")

        if type(data[0]) == float and type(data[1]) == float and type(data[2]) == float:
            if DEBUG:
                print("\n\n\nCorrect dimensions input.")
            self._body_length = data[0]
            self._body_width = data[1]
            self._body_height = data[2]
        else:
            self._body_length = 0
            self._body_width = 0
            self._body_height = 0

    @body_whl.getter
    def body_whl(self):
        params = list(self._body_length, self._body_width, self._body_height)
        return params

    @body_whl.deleter
    def body_whl(self):
        if DEBUG:
            print("\n\n\n Deleting Truck object with following object: ")
            get_info()
        del self._body_length
        del self._body_width
        del self._body_height
    


