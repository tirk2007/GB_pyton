def thesaurus(*names):
    list_name = [*names]
    dictionary = {}
    list_name_1 = []
    for name in list_name:
        name.capitalize()
        char = name[0]
        newnames = []
        dictionary.setdefault(char, newnames)
        newnames = dictionary.get(char)
        newnames.append(name)
        dict_1 = {char : newnames}
        dictionary.update(dict_1)
    return dictionary


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
