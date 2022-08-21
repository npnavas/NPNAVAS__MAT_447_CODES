def char_freq(msg):
    freqs = {}

    ## KEEP TRACK OF FREQUENCIES ##
    for char in msg:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1


    return dict(sorted(freqs.items(), key=lambda item: item[1]))

msg = 'GNNIMUKSUIPYVANGSUNYPYKUSCNUSBUHLQNYVOUPYKNGOYQPRVYNXGVRGNWGNWGNDIRYA'
print("Letter frequencies in msg in reverse order:\n", char_freq(msg))
