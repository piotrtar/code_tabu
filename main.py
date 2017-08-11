from view import *
from model import *
import controller


def main():
    Event.read_from_csv()
    controller.start()
    Event.write_to_csv()


if __name__ == "__main__":
    main()