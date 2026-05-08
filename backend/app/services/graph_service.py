def build_graph(text):

    words = text.split()

    filtered_words = []

    for word in words:

        clean_word = word.strip().lower()

        if (
            len(clean_word) > 6 and
            clean_word.isalpha()
        ):

            filtered_words.append(clean_word)

    unique_words = list(dict.fromkeys(filtered_words))

    selected_words = unique_words[:8]

    edges = []

    for i in range(len(selected_words) - 1):

        edges.append([
            selected_words[i],
            selected_words[i + 1]
        ])

    return edges