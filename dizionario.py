my_dict = {
    'orthogroup1': [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12']],
    'orthogroup2': [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['l', 'm', 'n']],
}

for value in my_dict.values():
    for org in range(len(value)):
        for gene in value[org]:
            for org_homo in range(org + 1, len(value)):
                for homologue in value[org_homo]:
                    print(gene, homologue)


