from abc import ABC, abstractmethod
import json
import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Abstract Base Class
class Tire(ABC):
    """
    Abstract base class representing a generic tire.
    """

    @abstractmethod
    def circumference(self):
        """
        Calculate the circumference of the tire.
        """
        pass

    @abstractmethod
    def surface_area(self):
        """
        Calculate the surface area of the tire.
        """
        pass


# Mixin for logging
class LogMixin:
    """
    Mixin for logging messages.
    """

    @staticmethod
    def log(message):
        logging.info(message)


# Mixin for serialization
class SerializationMixin:
    """
    Mixin for serializing objects to JSON.
    """

    def serialize(self):
        """
        Serialize the object to a JSON string.
        """
        return json.dumps(self.__dict__)


# Decorator for logging method calls
def logged(method):
    """
    Decorator to log method calls and their results.
    """

    def wrapper(*args, **kwargs):
        logging.info(f"Calling {method.__name__} with {args} and {kwargs}")
        try:
            result = method(*args, **kwargs)
            logging.info(f"{method.__name__} returned {result}")
            return result
        except Exception as e:
            logging.error(f"Error in {method.__name__}: {e}")
            raise

    return wrapper


# Concrete class for Car Tire
class CarTire(Tire, LogMixin, SerializationMixin):
    """
    Represents a car tire with a radius and width.
    """

    def __init__(self, radius, width):
        self._radius = radius
        self._width = width

    @logged
    def circumference(self):
        """
        Calculate the circumference of the car tire.
        """
        return 2 * math.pi * self._radius

    @logged
    def surface_area(self):
        """
        Calculate the surface area of the car tire.
        """
        return 2 * math.pi * self._radius * self._width

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value


# Concrete class for Bicycle Tire
class BicycleTire(Tire, LogMixin, SerializationMixin):
    """
    Represents a bicycle tire with a radius.
    """

    def __init__(self, radius):
        self._radius = radius
        self.pressure = 0

    @logged
    def circumference(self):
        """
        Calculate the circumference of the bicycle tire.
        """
        return 2 * math.pi * self._radius

    @logged
    def surface_area(self):
        """
        Calculate the surface area of the bicycle tire.
        """
        return math.pi * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @logged
    def inflate(self, pressure):
        """
        Inflate the bicycle tire to the specified pressure.
        """
        if pressure <= 0:
            raise ValueError("Pressure must be positive")
        self.pressure = pressure
        return f"Inflated to {pressure} PSI"

    @logged
    def deflate(self):
        """
        Deflate the bicycle tire.
        """
        self.pressure = 0
        return "Deflated"


# Concrete class for Motorcycle Tire
class MotorcycleTire(Tire, LogMixin, SerializationMixin):
    """
    Represents a motorcycle tire with a radius and width.
    """

    def __init__(self, radius, width):
        self._radius = radius
        self._width = width

    @logged
    def circumference(self):
        """
        Calculate the circumference of the motorcycle tire.
        """
        return 2 * math.pi * self._radius

    @logged
    def surface_area(self):
        """
        Calculate the surface area of the motorcycle tire.
        """
        return 2 * math.pi * self._radius * self._width

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @logged
    def burnout(self):
        """
        Perform a burnout.
        """
        return "Burnout performed"


# Concrete class for Truck Tire
class TruckTire(Tire, LogMixin, SerializationMixin):
    """
    Represents a truck tire with a radius and width.
    """

    def __init__(self, radius, width):
        self._radius = radius
        self._width = width

    @logged
    def circumference(self):
        """
        Calculate the circumference of the truck tire.
        """
        return 2 * math.pi * self._radius

    @logged
    def surface_area(self):
        """
        Calculate the surface area of the truck tire.
        """
        return 2 * math.pi * self._radius * self._width

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @logged
    def retread(self):
        """
        Retread the truck tire.
        """
        return "Retread performed"


# Concrete class for Racing Tire
class RacingTire(Tire, LogMixin, SerializationMixin):
    """
    Represents a racing tire with a radius and width.
    """

    def __init__(self, radius, width):
        self._radius = radius
        self._width = width

    @logged
    def circumference(self):
        """
        Calculate the circumference of the racing tire.
        """
        return 2 * math.pi * self._radius

    @logged
    def surface_area(self):
        """
        Calculate the surface area of the racing tire.
        """
        return 2 * math.pi * self._radius * self._width

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @logged
    def heat(self):
        """
        Heat the racing tire.
        """
        return "Heated"


# Concrete class for Off-road Tire
class OffroadTire(Tire, LogMixin, SerializationMixin):
    """
    Represents an off-road tire with a radius and width.
    """

    def __init__(self, radius, width):
        self._radius = radius
        self._width = width

    @logged
    def circumference(self):
        """
        Calculate the circumference of the off-road tire.
        """
        return 2 * math.pi * self._radius

    @logged
    def surface_area(self):
        """
        Calculate the surface area of the off-road tire.
        """
        return 2 * math.pi * self._radius * self._width

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @logged
    def mud(self):
        """
        Apply mud to the off-road tire.
        """
        return "Mud applied"


# Example usage
if __name__ == "__main__":
    car_tire = CarTire(0.35, 0.2)
    print(f"Car Tire circumference: {car_tire.circumference()} meters")
    print(f"Car Tire surface area: {car_tire.surface_area()} square meters")
    print(car_tire.serialize())

    bicycle_tire = BicycleTire(0.35)
    print(f"Bicycle Tire circumference: {bicycle_tire.circumference()} meters")
    print(f"Bicycle Tire surface area: {bicycle_tire.surface_area()} square meters")
    print(bicycle_tire.inflate(40))
    print(bicycle_tire.serialize())

    motorcycle_tire = MotorcycleTire(0.35, 0.2)
    print(f"Motorcycle Tire circumference: {motorcycle_tire.circumference()} meters")
    print(f"Motorcycle Tire surface area: {motorcycle_tire.surface_area()} square meters")
    print(motorcycle_tire.burnout())
    print(motorcycle_tire.serialize())

    truck_tire = TruckTire(0.35, 0.2)
    print(f"Truck Tire circumference: {truck_tire.circumference()} meters")
    print(f"Truck Tire surface area: {truck_tire.surface_area()} square meters")
    print(truck_tire.retread())
    print(truck_tire.serialize())

    racing_tire = RacingTire(0.35, 0.2)
    print(f"Racing Tire circumference: {racing_tire.circumference()} meters")
    print(f"Racing Tire surface area: {racing_tire.surface_area()} square meters")
    print(racing_tire.heat())
    print(racing_tire.serialize())

    offroad_tire = OffroadTire(0.35, 0.2)
    print(f"Off-road Tire circumference: {offroad_tire.circumference()} meters")
    print(f"Off-road Tire surface area: {offroad_tire.surface_area()} square meters")
    print(offroad_tire.mud())
    print(offroad_tire.serialize())
