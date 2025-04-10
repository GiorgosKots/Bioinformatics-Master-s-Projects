#### `code/suffix_trie_builder.py`

def suffixes(S):
    """
    Generate all suffixes of a given string S and return them sorted.

    Parameters:
    S (str): The input string.

    Returns:
    list: A list of tuples containing each suffix and its starting index.
    """
    if not S:
        return []
    return sorted((S[i:] + "$", i) for i in range(len(S)))

def build_trie(suffixes):
    """
    Build a suffix trie from a list of suffixes.

    Parameters:
    suffixes (list): A list of suffixes with their starting indices.

    Returns:
    dict: A nested dictionary representing the suffix trie.
    """
    trie = {"Root": {}}
    for pattern, _ in suffixes:
        current_node = trie["Root"]
        for char in pattern:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node[''] = {}
    return trie

def visualize_trie(trie, filename='trie', file_format='png'):
    """
    Visualize the suffix trie using Graphviz.

    Parameters:
    trie (dict): The suffix trie to visualize.
    filename (str): The name of the output file (without extension).
    file_format (str): The format of the output file (e.g., 'png', 'pdf').

    Returns:
    graphviz.Digraph: The Graphviz Digraph object.
    """
    dot = graphviz.Digraph()

    def add_edges(node, prefix):
        for key, subtrie in node.items():
            if key == '$':
                dollar_node = prefix + '$'
                dot.node(dollar_node, label='$')
                dot.edge(prefix, dollar_node)
                continue
            new_prefix = prefix + key
            dot.node(new_prefix, label=key)
            dot.edge(prefix, new_prefix)
            add_edges(subtrie, new_prefix)

    root = 'Root'
    dot.node(root)
    add_edges(trie["Root"], root)
    dot.render(filename, format=file_format, cleanup=True)
    return dot

def main(sequence, output_filename='trie', file_format='png'):
    """
    Main function to generate suffixes, build the trie, and visualize it.

    Parameters:
    sequence (str): The input DNA sequence.
    output_filename (str): The name of the output file for the visualization.
    file_format (str): The format of the output file.
    """
    suffixes_list = suffixes(sequence)
    print(f"Suffixes: {suffixes_list}")

    trie = build_trie(suffixes_list)
    print(f"Trie: {trie}")

    visualize_trie(trie, output_filename, file_format).view()

if __name__ == "__main__":
    # Example usage
    sequence = "GAGTAAGTCA"
    main(sequence, output_filename='original_trie', file_format='png')