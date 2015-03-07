print("This is a python script.")
import ipdb; ipdb.set_trace()
print("Starting to execute this file.")

a = "monkey"
b = "donuts"

def print_some_numbers():
    for num in range(1, 5):
        import ipdb; ipdb.set_trace()
        print(num)

import ipdb; ipdb.set_trace()
print("In the middle of execution..")

print_some_numbers()

print("all_done!")

import ipdb; ipdb.set_trace()
