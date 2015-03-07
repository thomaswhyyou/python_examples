# Example
some_list = [1, 2, 3, 4]

try:
    some_list[5]
except IndexError:
    print("Index error only!")
    raise
except:
    print("catch all!")
    raise
finally:
    print("done!")
