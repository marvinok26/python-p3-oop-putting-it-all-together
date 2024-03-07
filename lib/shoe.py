class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._condition = "Used"

    @property
    def brand(self):
        return self._brand

    @property
    def size(self):
        return self._size

    @property
    def condition(self):
        return self._condition

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"

# Example usage
if __name__ == "__main__":
    # Test case 1
    stan_smith = Shoe("Adidas", 9)
    assert stan_smith.brand == "Adidas"
    assert stan_smith.size == 9

    # Test case 2
    stan_smith.size = "not an integer"  # This will print the error message

    # Test case 3
    stan_smith.cobble()
    assert stan_smith.condition == "New"
