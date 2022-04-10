input1 = [4, 'abcd', 'acbd', 'aaab', 'acbd']
input2 = [5, 'pisang', 'goreng', 'enak', 'sekali', 'rasanya']
input3 = [11, 'Satu', 'Sate', 'Tujuh', 'Tusuk', 'Tujuh', 'Sate', 'Bonus', 'Tiga', 'Puluh', 'Tujuh', 'Tusuk']

hasil1 = []
hasil2 = []
hasil3 = []

def get_index_of_duplicate(seq):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set( x for x in seq if x in seen or seen_add(x) )
    # turn the set into a list (as requested)
    duplicates = list(seen_twice)
    list_duplicates = []

    for d in duplicates:
        dupes = []
        for idx, val in enumerate(seq):
            if val == d:
                dupes.append(idx)

        list_duplicates.append(dupes)
    
    if len(list_duplicates) > 0:
        if len(list_duplicates) > 1:
            
            the_first = 0
            for idx, val in enumerate(list_duplicates):
                if idx > 0:
                    if val[1] < temp_val:
                        the_first = idx
                temp_val = val[1]    

            list_duplicate = list_duplicates[the_first]
                
        else:
            list_duplicate = list_duplicates[0]
    else:
        list_duplicate = 'false'

    return list_duplicate

print(get_index_of_duplicate(input1))
print(get_index_of_duplicate(input2))
print(get_index_of_duplicate(input3))