""" Function to remove dublicates from array
and keep the same order
"""
def remove_dubs(array):
    no_dubs = []
    for i in array:
        if i not in no_dubs:
            no_dubs.append(i)
    return no_dubs

if __name__ == "__main__":
    array = input('Please enter array items (separated by spaces):\n').split()
    print(type(array))
    result = remove_dubs(array)
    print(f"Removed dublicates:{result}")