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

#recursion
def get_sequence(number_of_hops, start_position, cache, sequence=None):
    if sequence is None:
        sequence = [start_position]

    if number_of_hops == 0:
        yield sequence
        return

    if ((start_position, number_of_hops)) in cache:
        yield cache[(start_position, number_of_hops)]
        return

    for neighbor in neighbors(start_position):
        yield from get_sequence(number_of_hops - 1, neighbor, cache, sequence + [neighbor])
        cache[(start_position, number_of_hops)] = sequence + [neighbor]

def get_nums_new(n):
    if n <= 0:
        return []

    start_position = 0
    results = []
    cache = {}
    for sequence in get_sequence(n, start_position, cache):
        results.append(sequence)
    return results


if __name__ == '__main__':
    print(get_nums_new(3))
    
