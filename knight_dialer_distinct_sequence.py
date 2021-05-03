def neighbors(k):
    d = {
        0: [4, 6],
        1: [8, 6],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [7, 0, 1],
        7: [2 ,6],
        8: [1, 3],
        9: [2 ,4],
    }
    return d[k]

def count_sequence(start_position, number_of_hops, cache):                  
    if number_of_hops == 0:                                           
        return 1                                                

    if ((start_position, number_of_hops)) in cache:
        return cache[(start_position, number_of_hops)]
       
    num_of_sequences = 0                                           
    for neighbor in neighbors(start_position):                  
        num_of_sequences += count_sequence(neighbor, number_of_hops - 1, cache)
        cache[(start_position, number_of_hops)] = num_of_sequences
    return num_of_sequences

def get_nums_memo(n):
    start_position = 0
    cache = {}
    return count_sequence(start_position, n, cache)

if __name__ == '__main__':
    print(get_nums_memo(3))
