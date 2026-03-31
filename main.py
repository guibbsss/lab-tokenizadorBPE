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


def merge_vocab(pair, v_in):

    v_out = {}

    bigram = ' '.join(pair)

    replacement = ''.join(pair)

    for word in v_in:

        new_word = word.replace(bigram, replacement)

        v_out[new_word] = v_in[word]

    return v_out


best = max(stats, key=stats.get)

print("melhor par:", best)

vocab = merge_vocab(best, vocab)

print(vocab)

num_merges = 5

for i in range(num_merges):

    stats = get_stats(vocab)

    best = max(stats, key=stats.get)

    print("iteracao", i+1)
    print("par escolhido:", best)

    vocab = merge_vocab(best, vocab)

    print("vocab atualizado:")
    print(vocab)

    print("--------------------------------------------------")