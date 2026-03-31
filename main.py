vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}


def get_stats(vocab):

    pairs = {}

    for word, freq in vocab.items():

        symbols = word.split()

        for i in range(len(symbols) - 1):

            pair = (symbols[i], symbols[i+1])

            if pair not in pairs:
                pairs[pair] = 0

            pairs[pair] += freq

    return pairs


stats = get_stats(vocab)

print(stats)