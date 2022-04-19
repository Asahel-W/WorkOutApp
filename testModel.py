from model import *


def main():
    model = CreateDB("example.db")
    print("Test Model")
    input_str = input("> ")
    while input_str != "exit":
        model.updateDB(input_str)
        input_str = input("> ")


main()
