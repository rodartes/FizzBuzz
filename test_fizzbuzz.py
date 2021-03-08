import fizzbuzz

def test_fizz():
  three_muls = [3, 6, 9, 12, 18, 21, 24, 27, 33, 36, 39, 42, 48, 51]
  for x in three_muls:
    assert fizzbuzz.fizzbuzz(x) == "Fizz"

def test_buzz():
  five_muls = [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100]
  for x in five_muls:
   assert fizzbuzz.fizzbuzz(x) == "Buzz"

def test_fizzbuzz():
  three_five_muls = [15, 30, 45, 60, 75, 90]
  for x in three_five_muls:
    assert fizzbuzz.fizzbuzz(x) == "FizzBuzz"

def test_nofizzbuzz():
  non_muls = [1, 2, 4, 7, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29,31]
  for x in non_muls:
    assert fizzbuzz.fizzbuzz(x) == x