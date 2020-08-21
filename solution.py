from os.path import splitext


DEBUG = True


class CarBase:

    def __init__(self, brand, photo_file_name, carrying, car_type=None):
        if DEBUG:
            print("Initializing CarBase object: ")
            print("Car type: ", car_type)
            print("Brand: ", brand)
            print("Photo file name: ", photo_file_name)
            print("Carrying: ", carrying, "\n")

        self._car_type = car_type
        self._photo_file_name = photo_file_name
        self._brand = brand
        self._carriyng = carrying

    def get_photo_file_ext(self):
        pass

    def get_info(self):
        print("CarBase object information:")
        print("Car type: ", self._car_type)
        print("Brand: ", self._brand)
        print("Photo file name: ", self._photo_file_name)
        print("Carrying: ", self._carriyng)

