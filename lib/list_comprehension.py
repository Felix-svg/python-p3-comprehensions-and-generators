#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [num for num in num_list if num % 2 == 0]
    return even_nums

even_nums = return_evens([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(even_nums)

def make_exclamation(sentence_list):
    exclamations = [sentence + "!" for sentence in sentence_list]
    return exclamations

new_sentence = make_exclamation(["Hello", "World"])
print(new_sentence)