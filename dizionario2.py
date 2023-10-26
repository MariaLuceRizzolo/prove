from itertools import combinations

my_dict = {
    'orthogroup1': [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12']],
    'orthogroup2': [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['l', 'm', 'n']],
}

for group_name, group_values in my_dict.items():
    for genes1, genes2 in combinations(group_values, 2):
        for gene1 in genes1:
            for gene2 in genes2:
                print(gene1, gene2)

