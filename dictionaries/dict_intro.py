# dict is a key value pair
sentence = ["the", "is", "a", "the"]
my_dict = {}
for i in sentence:
    my_dict[i] = my_dict.get(i, 0) + 1

print(my_dict)
