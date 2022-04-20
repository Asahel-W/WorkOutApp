from model import *


def main():
    model = CreateDB("example.db")
    print("Test Model")
    input_str = input("sqlite3> ")
    while input_str != "exit":
        model.updateDB(input_str)
        input_str = input("sqlite3> ")


main()
