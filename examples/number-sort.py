from number_sort import sorter


def runTests(numbers: list[int]):
    a = sorter.highestToLowest(numbers)
    b = sorter.lowestToHighest(numbers)
    c = sorter.getLargest(numbers)
    d = sorter.getSmallest(numbers)

    print(a, b, c, d)


if __name__ == "__main__":
    numberArray = [3, 4, 5, 6, 7, 4, 5]
    runTests(numberArray)
