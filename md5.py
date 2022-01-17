from ast import If
import hashlib

def converter():
    while True:
        my_input = input("Enter the word to convert: ")
        x = hashlib.md5(my_input.encode('utf-8')).hexdigest()
        print(x)
        if my_input == "exit()":
            print("Byeeeee!")
            break

converter()