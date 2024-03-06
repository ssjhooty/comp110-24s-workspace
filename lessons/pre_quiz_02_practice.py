# While  loop
stats: list[int] = [7, 8, 9]
index: int = 0
total: int = 100
while index < len(stats):
    total -= stats[index]
    index += 1

# For ... in  loop
stats: list[int] = [7, 8, 9]
total: int = 100
for elem in stats:
    total -= elem

# For ... in range  loop
stats: list[int] = [7, 8, 9]
total: int = 100
for index in range(0, len(stats)):
    total -= stats[index]




# Short words code writing drill
# def short_words(my_list: list[str]) -> str:
    # """Returns list of words that are shorter than 5 characters."""
    # for elem in my_list:
        # if len(elem) <= 5:
            # return elem
        # else:
            # print ("f{elem} is too long!")

# short_words()

# Corrected version

def short_words(my_list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    ret_list: list[str] = []
    for elem in my_list:
        if len(elem) <= 5:
            ret_list.append(elem)
        else:
            print ("f{elem} is too long!")
    return ret_list

my_list = ["sun", "cloud", "sky"]
print(short_words(my_list))