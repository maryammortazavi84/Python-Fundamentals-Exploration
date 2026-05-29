def queranumeric(order: list[str], words: list[str]) -> list[str]:
    return sorted(
        words,
        key=lambda word: ranking(order, word)
    )


    
    


def ranking(order: list[str], word: str) -> list[int]:
    ranks = []
    for letter in word:
        if letter in order:
            ranks.append(order.index(letter))
        else:
            ranks.append(len(order))
    return ranks
        

