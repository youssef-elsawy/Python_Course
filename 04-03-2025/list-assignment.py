# exercise 1
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
uppercased_fruits=[fruit.upper() for fruit in fruits]
print(f"exercise 1:\t {uppercased_fruits}")

# exercise 2
capitalized_fruits=[fruit.capitalize() for fruit in fruits]
print(f"exercise 2:\t {capitalized_fruits}")

# exercise 3
fruits_with_more_than_two_vowels=[fruit for fruit in fruits if (fruit.count("a") + fruit.count("e") + fruit.count("i") + fruit.count("o") + fruit.count("u")) >2]
print(f"exercise 3:\t {fruits_with_more_than_two_vowels}")

# exercise 4
fruits_with_only_two_vowels=[fruit for fruit in fruits if (fruit.count("a") + fruit.count("e") + fruit.count("i") + fruit.count("o") + fruit.count("u")) ==2]
print(f"exercise 4:\t {fruits_with_only_two_vowels}")

# exercise 5
fruits_with_more_than_5_chars=[fruit for fruit in fruits if (len(fruit)) >5]
print(f"exercise 5:\t {fruits_with_more_than_5_chars}")

# exercise 6
fruits_with_exactly_5_chars=[fruit for fruit in fruits if (len(fruit)) ==5]
print(f"exercise 6:\t {fruits_with_exactly_5_chars}")

# exercise 7
fruits_with_less_than_5_charss=[fruit for fruit in fruits if (len(fruit)) <5]
print(f"exercise 7:\t {fruits_with_less_than_5_charss}")

# exercise 8
number_in_each_fruit=[len(fruit) for fruit in fruits]
print(f"exercise 8:\t {number_in_each_fruit}")

# exercise 9
fruits_with_letter_a=[fruit for fruit in fruits if "a" in fruit]
print(f"exercise 9:\t {fruits_with_letter_a}")

# exercise 10
even_numbers=[n for n in numbers if (n %2) ==0]
print(f"exercise 10:\t {even_numbers}")

# exercise 11
odd_numbers=[n for n in numbers if (n %2) !=0]
print(f"exercise 11:\t {odd_numbers}")

# exercise 12
positive_numbers=[n for n in numbers if n>0]
print(f"exercise 12:\t {positive_numbers}")

# exercise 13
negative_numbers=[n for n in numbers if n<0]
print(f"exercise 13:\t {negative_numbers}")